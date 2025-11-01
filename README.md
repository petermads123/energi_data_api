# Energi data APIs
This repo is for implementing various APIs

## Energidataservice
Energinets energidataservice, following api's are implemented:
- DayAheadPrices (energidataservice.get_day_ahead_prices)
- Tariffs (TBD)

## Eloverblik
Energinets datahub eloverblik, api for collecting local meter data
- Meter data (eloverblik.get_meter_data) (TBD)

## Development setup
### First time setup
1. Make sure ruff is installed in your vscode
- In settings.json have the following lines pasted:

    "python.linting.enabled": true,
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": true,
        "source.fixAll.ruff": true,
        "source.organizeImports": true
    },
    "ruff.lint.enable": true,
    "ruff.format.enable": true,

2. If on windows make sure "make" is installed in the base environment using "conda install -c conda-forge make"
- Restart your terminal
3. Run "make setup" in the terminal to create/update the environment with all dependencies automatically installed

### Updating environment
Whenever you need to update the packages, run "make setup"
Environment can be activated by "conda activate <env_name>" or by using the environment menu in the bottom left corner (vscode)