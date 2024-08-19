#!/bin/bash -e

script_file=$(readlink -e "${BASH_SOURCE[0]}")
root_dir="${script_file%/*}"

openapi-generator-cli generate \
  --input-spec "${root_dir}/openapi.json" \
  --generator-name typescript-fetch \
  --output "${root_dir}"
