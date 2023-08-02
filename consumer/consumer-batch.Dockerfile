FROM python:3.8.3-slim

COPY ./consumer/requirements.txt /consumer_batch/requirements.txt
COPY ./consumer/src /consumer_batch
COPY ./.env /consumer_batch/.env
WORKDIR /consumer_batch

RUN pip install -U -r requirements.txt

ENTRYPOINT ["python", "batch_consumer.py"]