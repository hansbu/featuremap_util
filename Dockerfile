FROM python:3.7
COPY . /app
WORKDIR /app
RUN apt-get -y update; apt-get -y upgrade
RUN apt-get -y install openslide-tools python3-openslide
#RUN apt-get -y install build-essential cmake unzip pkg-config
RUN pip install -r requirements.txt
WORKDIR /app

