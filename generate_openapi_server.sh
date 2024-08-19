#!/bin/bash -e

script_file=$(readlink -e "${BASH_SOURCE[0]}")
host_dir="${script_file%/*}"

docker run --rm \
  -v "${host_dir}:/host" \
  openapitools/openapi-generator-cli generate \
  --input-spec /host/openapi.json \
  --generator-name python-aiohttp \
  --output /host \
  --package-name llm_server \
  --additional-properties packageVersion=0.0.1

make format
