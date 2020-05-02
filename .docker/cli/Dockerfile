FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/local/makeup/
WORKDIR /usr/local/makeup/
COPY requirements.txt /usr/local/makeup/
RUN pip install -r requirements.txt
