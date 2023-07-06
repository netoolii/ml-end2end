#!/usr/bin/env bash

set -e

mkdir ./app/apis
mkdir ./app/assets
mkdir ./app/clients
mkdir ./app/dao
mkdir ./app/handlers
mkdir ./app/helpers
mkdir ./app/models
mkdir ./app/services

touch ./app/requirements.txt
touch ./app/app.py
touch ./app/__init__.py

touch ./app/apis/__init__.py
touch ./app/assets/__init__.py
touch ./app/clients/__init__.py
touch ./app/dao/__init__.py
touch ./app/handlers/__init__.py
touch ./app/helpers/__init__.py
touch ./app/models/__init__.py
touch ./app/services/__init__.py


touch ./app/services/gunicorn.config.py
