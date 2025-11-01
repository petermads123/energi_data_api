"""This is a generic API class for data from energidataservice.dk."""

import pandas as pd
import requests

from utils import fix_tz
from wrappers import retry


class EnergiDataServiceAPI:
    """Generic API class for data from energidataservice.dk."""

    BASE_URL = "https://api.energidataservice.dk/dataset/"

    def __init__(self) -> None:
        """Initialize the EnergiDataServiceAPI class."""

    def call(
        self,
        dataset: str,
        start: str | pd.Timestamp,
        end: str | pd.Timestamp,
        params: dict | None = None,
    ) -> pd.DataFrame:
        """Call the API for a specific dataset and time range.

        Args:
            dataset (str): The dataset name.
            start (str | pd.Timestamp): The start date/time.
            end (str | pd.Timestamp): The end date/time.
            params (dict | None): Additional parameters for the API call. Default is None.

        Returns:
            pd.DataFrame: The data retrieved from the API.
        """
        start = fix_tz(start)
        end = fix_tz(end)

        url = self.BASE_URL + dataset

        # Build parameters and add additional params
        parameters = {
            "start": start.strftime("%Y-%m-%dT%H:%M"),
            "end": end.strftime("%Y-%m-%dT%H:%M"),
            "timezone": "UTC",
            "sort": "TimeUTC asc",
        }
        parameters.update(params)

        # Call the API
        result = self._call_api(url, parameters)

        # Convert to DataFrame
        df = pd.DataFrame(result.get("records"))

        # Rename time columns to standard names and make timestamp
        if "TimeUTC" in df.columns:
            df.rename(columns={"TimeUTC": "UTC"}, inplace=True)
            df["UTC"] = pd.to_datetime(df["UTC"]).dt.tz_localize("UTC")

        if "TimeDK" in df.columns:
            df.rename(columns={"TimeDK": "CET"}, inplace=True)
            df["CET"] = df["UTC"].dt.tz_convert("CET")

        return df

    @retry()
    def _call_api(self, url: str, params: dict) -> dict:
        """Internal method to call the API and return JSON response.

        Notes:
            - retry wrapper is used to handle retries on failures.

        Args:
            url (str): The full URL for the API call.
            params (dict): The parameters for the API call.

        Returns:
            dict: The JSON response from the API.
        """
        # Calling the API
        response = requests.get(url, params=params)

        # Raise an error for bad responses
        response.raise_for_status()

        # Return JSON result
        result = response.json()
        return result
