FROM python:3.8.3-slim

COPY ./consumer/requirements.txt /consumer_update/requirements.txt
COPY ./consumer/src /consumer_update
COPY ./.env /consumer_update/.env
WORKDIR /consumer_update

RUN pip install -U -r requirements.txt

ENTRYPOINT ["python", "update_consumer.py"]