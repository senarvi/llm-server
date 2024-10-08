#!/bin/bash -e

script_file=$(readlink -e "${BASH_SOURCE[0]}")
root_dir="${script_file%/*}"

openapi-generator-cli generate \
  --input-spec "${root_dir}/openapi.json" \
  --generator-name python-aiohttp \
  --output "${root_dir}" \
  --package-name llm_server \
  --additional-properties packageVersion=0.0.1

make format
