#!/bin/bash

# Build a python virtual environment and install dependencies listed in the requirements.txt file

python3 -m venv env

source env/bin/activate

python3 -m pip install -r requirements.txt

deactivate