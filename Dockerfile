FROM python:3.7
COPY ./csv_to_json /usr/bin
COPY . /app
WORKDIR /app
RUN apt-get -y update; apt-get -y upgrade
RUN apt-get -y install openslide-tools python3-openslide vim
#RUN apt-get -y install build-essential cmake unzip pkg-config
RUN pip install -r requirements.txt
WORKDIR /app
