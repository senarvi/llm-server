# LLM server

## Code Generation

The LLM server was generated using the [OpenAPI Generator](https://openapi-generator.tech). It uses the
[Connexion](https://github.com/zalando/connexion) library on top of aiohttp. To regenerate the server code, run the
following:

```
openapi-generator-cli generate \
  --input-spec openapi.json \
  --generator-name python-aiohttp \
  --output . \
  --package-name llm_server \
  --additional-properties packageVersion=0.0.1
```

The client code can be generated for various frameworks. To regenerate the TypeScript client code, run the following:

```
openapi-generator-cli generate \
  --input-spec openapi.json \
  --generator-name typescript-fetch \
  --output .
```

Add edited files to _.openapi-generator-ignore_ to prevent generator from overwriting them. Typically:

```
server/controllers/*
test/*
*.txt
```

## Usage

To run the API, execute the following from the root directory:

```
pip install -r requirements.txt
python -m llm_server
```

You can test the API using curl:

```
curl\
  -X POST\
  -H 'Content-Type: application/json'\
  -d '{"review":"my movie review","reviewer":"my reviewer"}'\
  'http://localhost:8080/movie_summary'
```

To launch the integration tests, use pytest:

```
pip install -r test-requirements.txt
pytest tests -v
```
