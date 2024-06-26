#!/usr/bin/env bash

set -e

echo "Criando estrutura de pastas"

mkdir -p ./app/apis
mkdir ./app/clients
mkdir ./app/handlers
mkdir ./app/helpers
mkdir ./app/models


touch ./app/__init__.py
touch ./app/apis/__init__.py
touch ./app/clients/__init__.py
touch ./app/handlers/__init__.py
touch ./app/helpers/__init__.py
touch ./app/models/__init__.py

touch ./app/requirements.txt
touch ./app/app.py
touch ./app/database.py
touch ./app/helpers/gunicorn.config.py
touch ./app/helpers/commom.py
touch ./app/helpers/env_helper.py
touch ./app/helpers/db_connect.py
touch ./app/apis/health_check.py
touch ./app/models/users.py