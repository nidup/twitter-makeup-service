FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/local/myapp/
WORKDIR /usr/local/myapp/
COPY requirements.txt /usr/local/myapp/
RUN pip install -r requirements.txt
