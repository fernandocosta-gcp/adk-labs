# ADK Labs Monorepo
## by @fernandocosta

## Pre-Req

### (For Linux)
Install venv first if you haven't:
sudo apt install python3.11-venv

Create a new venv:
VENV_PATH=~/venvs/adk-quickstart
command -v deactivate >/dev/null 2>&1 && deactivate
rm -rf $VENV_PATH \
    && python3.11 -m venv $VENV_PATH \
    && source $VENV_PATH/bin/activate
pip install google-adk


### (For Mac)
VENV_PATH=~/venvs/adk-quickstart
command -v deactivate >/dev/null 2>&1 && deactivate
rm -rf $VENV_PATH \
    && python3.11 -m venv $VENV_PATH \
    && source $VENV_PATH/bin/activate
pip install google-adk

## Monorepo detail
This repository contains multiple ADK lab projects:
- `lab011/`: Quickstart project and basic agent.
- `lab022/`: Multiagent, parent agents, pair agent and subagent concepts.
- `lab033/`: Sequential Agent pattern
- `lab044/`: Loop Agent pattern
- `lab055/`: Parallel Agent pattern

