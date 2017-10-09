FROM ubuntu:latest

MAINTAINER Ala Eddine CHHIMA "alaeddine.chhima@riminder.net"

RUN apt-get update -y 
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT python app.py
