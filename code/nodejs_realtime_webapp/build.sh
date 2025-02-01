#!/bin/bash

docker build -t ephemeral_server -f Dockerfile.ephemeral_server --no-cache .
docker build -t web -f Dockerfile.web --no-cache .
