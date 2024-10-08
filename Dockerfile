FROM python:3.12

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

COPY llm_server/ /llm_server

WORKDIR /
ENTRYPOINT ["python", "-m", "llm_server"]
