FROM python:alpine3.20

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt