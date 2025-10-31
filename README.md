# template_repo
This is a template repo for creating new projects

## Setup
1. To setup this repo first choose a name set this name in pyproject.toml, environment.yml and Makefile
2. Define dependencies withing pyproject.toml
3. Make sure ruff is installed in your vscode
- In settings.json have the following lines pasted:
    "python.linting.enabled": true,
    "editor.defaultFormatter": "charliermarsh.ruff", 
    "editor.formatOnSave": true,
    "ruff.lint.enable": true,
    "ruff.format.enable": true
4. If on windows make sure "make" is installed in the base environment using "conda install -c conda-forge make"
- Restart your terminal
4. Run "make setup" in the terminal to create/update the environment with all dependencies automatically installed

## Updating
Whenever you need to update the packages, run "make setup"
Environment can be activated by "conda activate <env_name>" or by using the environment menu in the bottum left corner (vscode)