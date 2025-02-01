#!/bin/bash

docker run --rm -d -p 3000:3000 -e OPENAI_API_KEY=${OPENAI_API_KEY} ephemeral_server
sleep 3
docker run --rm -it -p 8080:80 -v /home/carwyn/dev/cognitive_warmup/code/python_generator/output:/usr/share/nginx/html/data -e OPENAI_API_KEY=${OPENAI_API_KEY} web