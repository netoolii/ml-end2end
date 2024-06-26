#!/usr/bin/env bash

set -e

TAG="$1"


if [[ -z "$TAG" ]]; then
   TAG="1.0"
fi


echo "Building backend image as tag: ${TAG}"
docker build . -t backend:"${TAG}" --rm   

sleep 5

echo "Running backend container"
docker run -v "./app:/app" -p 8080:8080 --name backend  --rm backend:"${TAG}"