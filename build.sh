#!/usr/bin/env bash

PROGNAME=$(basename "$0")
# Output colors
NORMAL="\\033[0;39m"
RED="\\033[1;31m"
# Check input
 if [[ "$#" -eq  "0" ]]
   then
     echo "No arguments supplied"
     printf "    ${RED}usage: $PROGNAME /path/to/input/dir /path/to/output/dir /path/to/wsi/dir$1${NORMAL}\n"
     exit 1
 fi

# Names to identify images and containers of this app
IMAGE_NAME='featuremap_util'
CONTAINER_NAME="quip-maputil" # NAME TBA

build() {
  docker build -t $IMAGE_NAME .
  docker run --name "$CONTAINER_NAME" -v $1:/data/input -v $2:/data/output -v $3:/data/wsi -itd "$IMAGE_NAME"
  # docker run --name "$CONTAINER_NAME" -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output -v $HOME/images1/brca:/data/wsi -itd "$IMAGE_NAME"
}

build $1 $2 $3
