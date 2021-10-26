#!/bin/bash

# First time initializing the database
# Changes to the model or changes to the database
python3 manage.py makemigrations

# Applying migrations
# Creates db.sqlite3
python3 manage.py migrate

python3 manage.py runserver