#!/bin/bash

echo "Hola!! What is your name? "

read Who

echo "Welcome $Who!"

if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

#include txt file with more intructions 

python3 cc_app.py







# Create a venv environment" 
# python3 -m venv ./venv

# echo "2. Activate the venv environment" 
# source venv/bin/activate

# echo "3. You can start now" 
# python3 cc_app.py





#Create  a vnenv enviroment 
# python3 -m vnenv./ vnenv

#Once you activate the 
# python menu.py
