#!/bin/bash -e

docker build -t senarvi/llm-server:latest .
docker push senarvi/llm-server:latest
