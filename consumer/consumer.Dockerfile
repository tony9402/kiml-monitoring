FROM python:3.8.3-slim

# COPY ./kiml-api/requirements.txt /kiml-api/requirements.txt
# COPY ./kiml-api/src /kiml-api
# COPY .env /kiml-api/.env
# WORKDIR /kiml-api

# RUN pip install -U -r /kiml-api/requirements.txt

ENTRYPOINT ["python", "main.py"]