"""Function to call the EnergiDataService day ahead prices API."""

import pandas as pd

from energidataservice import EnergiDataServiceAPI
from utils import fix_tz


def get_day_ahead_prices(
    start: str | pd.Timestamp,
    end: str | pd.Timestamp | None = None,
    bidding_zone: str | list[str] | None = None,
    tz: str = "CET",
) -> pd.DataFrame:
    """Get day ahead prices for specified bidding zones and time range.

    Args:
        start (str | pd.Timestamp): The start date/time.
        end (str | pd.Timestamp | None, Optional): The end date/time. Default is None.
        bidding_zone (str | list[str] | None, Optional): The bidding zone(s) to filter by. Default is None.
        tz (str, Optional): The time zone to assume the input dates have. Default is "CET".

    Returns:
        pd.DataFrame: ["UTC", "CET", "PriceArea", "DayAheadPriceEUR", "DayAheadPriceDKK"]
    """
    # Make sure bidding_zone is a list
    if isinstance(bidding_zone, str):
        bidding_zone = [bidding_zone]

    # Assume input is in CET timezone, change to UTC
    start = fix_tz(start, tz_from=tz, tz_to="CET")
    # If end is None, set to start + 1 day (CET)
    end = (
        (start + pd.DateOffset(days=1))
        if end is None
        else fix_tz(end, tz_from=tz, tz_to="CET")
    )

    start = start.tz_convert("UTC")
    end = end.tz_convert("UTC")

    # Add parameters
    params = {}
    if bidding_zone:
        params["filter"] = f"{{'PriceArea':{bidding_zone}}}".replace("'", '"')

    # Call the API
    df = EnergiDataServiceAPI().call(
        dataset="DayAheadPrices",
        start=start,
        end=end,
        params=params,
    )

    return df


if __name__ == "__main__":
    df = get_day_ahead_prices(start="2025-10-25", end="2025-10-27", bidding_zone="DK2")
    print(df)
