#!/usr/bin/env bash

set -e

docker run -d -v "databasedata:/var/lib/mysql" --name mariadb --rm --net=services-network mariadb:1.0

docker run -d -p 8081:80 --name phpmyadmin --net=services-network --rm phpmyadmin:1.0

docker run -d --name ollama --net=services-network --rm ollama:2.0
