#!/bin/bash

# Use python3 instead of python
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
