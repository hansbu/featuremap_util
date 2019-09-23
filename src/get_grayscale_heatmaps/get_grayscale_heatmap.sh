#!/bin/bash

#source ../../conf/variables.sh

# Path contains the svs slides
# This is just used for getting the height and width
# of the slides
SLIDES='/data/wsi'
EXT="$1"

# Locations of unmodified heatmaps
# The filenames of the unmodifed heatmaps should be:
#   prediction-${slide_id}
# For example:
#   prediction-TCGA-NJ-A55O-01Z-00-DX1
HEAT_LOC='/data/input'
#rm grayscale_heatmaps/*

for files in ${HEAT_LOC}/color-*; do

  # Get slide id
  SVS=$(echo ${files} | awk -F'/' '{print $NF}' | awk -F'color-' '{print $2}')

  # Find the unmodified heatmap
  PRED=$(ls -1 ${HEAT_LOC}/prediction-${SVS}* | grep -v low_res)
  COLOR=${files}

  SVS_FILE=`ls -1 ${SLIDES}/${SVS}*.$EXT | head -n 1`
  if [ ! -f ${SVS_FILE} ]; then
    echo ${SLIDES}/${SVS}.XXXX.$EXT does not exist.
    continue;
  fi

  WIDTH=$(openslide-show-properties ${SVS_FILE} |
    grep "openslide.level\[0\].width" | awk '{print substr($2,2,length($2)-2);}')
  HEIGHT=$(openslide-show-properties ${SVS_FILE} |
    grep "openslide.level\[0\].height" | awk '{print substr($2,2,length($2)-2);}')

  python /app/src/get_grayscale_heatmaps/get_grayscale_heatmap.py ${SVS} ${WIDTH} ${HEIGHT} ${PRED} ${COLOR}
done
#cp ./grayscale_heatmaps/* ${GRAYSCALE_HEATMAPS_PATH}/

exit 0
