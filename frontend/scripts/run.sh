#!/usr/bin/env bash

set -e

# TAG="$1"


# if [[ -z "$TAG" ]]; then
#    TAG="1.0"
# fi


NODE_ENV="development" 
HOST="0.0.0.0"
CHOKIDAR_USEPOLLING=true
WATCHPACK_POLLING=true


docker build . --target builder -t frontend:1.0 --rm


docker run --name frontend \
        -p "3000:3000" \
        --net=services-network \
        --env NODE_ENV="${NODE_ENV}" \
        --env HOST="${HOST}" \
        --env CHOKIDAR_USEPOLLING="${CHOKIDAR_USEPOLLING}" \
        --env WATCHPACK_POLLING="${WATCHPACK_POLLING}" \
        -v "./app:/app" \
        -v "node_modules:/app/node_modules" \
        --rm \
        frontend:1.0 \
        yarn dev
        
