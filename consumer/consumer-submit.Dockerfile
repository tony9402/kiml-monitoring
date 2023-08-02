FROM python:3.8.3-slim

RUN apt update
RUN apt install -y git

COPY ./consumer/requirements.txt /consumer_submit/requirements.txt
COPY ./consumer/src /consumer_submit
COPY ./.env /consumer_submit/.env
WORKDIR /consumer_submit

RUN pip install -U -r requirements.txt

ENTRYPOINT ["python", "submit_consumer.py"]