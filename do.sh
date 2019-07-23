#!/usr/bin/env bash

PROGNAME=$(basename "$0")

# Output colors
NORMAL="\\033[0;39m"
RED="\\033[1;31m"
BLUE="\\033[1;34m"

# Names to identify images and containers of this app
IMAGE_NAME='featuremap_util'
CONTAINER_NAME="jsonic" # NAME TBA

log() {
  printf "$BLUE > $1$NORMAL\n"
}

error() {
  echo ""
  printf "${RED}>>> ERROR - $1${NORMAL}\n"
}

build() {
  docker build -t $IMAGE_NAME .

  [[ $? != 0 ]] && \
    error "Docker image build failed !" && exit 100

  [[ $? == 0 ]] && \
    log "Docker image build succeeded !" && exit 000
}

run() {
  docker run --name "$CONTAINER_NAME" -v $1:/data/input -v $2:/data/output -v $3:/data/wsi -itd "$IMAGE_NAME"
  # docker run --name "$CONTAINER_NAME" -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output -itd "$IMAGE_NAME"
}

checkinput() {
  if [[ $# -eq 0 ]]
  then
    error "No arguments supplied"
    echo "usage: $PROGNAME /path/to/input/dir /path/to/output/dir /path/to/wsi/dir"
    exit 100
  else
    build
    run $1 $2 $3
  fi
}
checkinput
