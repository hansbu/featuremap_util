FROM python:3.7
#COPY ./csv_to_json /usr/bin
COPY ./bin/* /usr/bin/
COPY . /app
WORKDIR /app
RUN apt-get -y update; apt-get -y upgrade
RUN apt-get -y install vim openslide-tools python3-openslide python3-opencv
RUN pip install -r requirements.txt
WORKDIR /app
