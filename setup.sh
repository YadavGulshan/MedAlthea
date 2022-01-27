#!/usr/bin/env bash

# This file will just export the .env variables to the shell
export $(cat .env | xargs)
echo "Environment variables exported"


# Check if virtual env exist for python or not
if [ ! -d "env" ]; then
    echo "Creating virtual environment"
    python3 -m venv env
    echo "Virtual environment created"
fi


# start the virtual environment for python
source env/bin/activate


# install the requirements
pip install -r requirements.txt


cd backend

# Check if fish is installed
if [ -f /usr/bin/fish ]; then
    fish
else
    echo "Fish is not installed"
fi

exit