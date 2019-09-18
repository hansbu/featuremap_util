FROM python:3.7
COPY ./bin/* /usr/bin/
COPY . /app
RUN apt-get -y update; apt-get -y upgrade
RUN apt-get -y install git vim uuid-runtime openslide-tools python3-openslide python3-opencv
#private dir, setup login...
#CMD ["/usr/bin/git_grayscale_heatmaps"]
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /app
