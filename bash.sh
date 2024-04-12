#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install django

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

