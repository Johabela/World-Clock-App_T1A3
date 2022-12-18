#!/bin/bash

echo "Hola!! What is your name? "

read Who

echo "Welcome $Who!"

if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://www.python.org/' >&2
  exit 1
fi

python3 cc_app.py



