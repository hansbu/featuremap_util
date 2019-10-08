#!/usr/bin/env bash

PROGNAME=$(basename "$0")
error_exit() {
  echo "${PROGNAME}: ${1:-"Error"}" 1>&2
  echo "Line $2"
  exit 1
}
ext="$1"
output_dir="$2"

#source ../../conf/variables.sh

# This is just used for getting wsi height and width
SLIDES='/data/wsi'

# Locations of unmodified heatmaps
# The filenames of the unmodifed heatmaps should be:
#   prediction-${slide_id}
# For example:
#   prediction-TCGA-NJ-A55O-01Z-00-DX1
HEAT_LOC='/data/input'
#rm grayscale_heatmaps/*

# We get the images based on what's in this heatmap_txt folder
for files in ${HEAT_LOC}/color-*; do

  if [ ${files[0]} == "/data/input/color-*" ]; then
    error_exit "There are no color files." $LINENO
  fi

  # From the color- prefix, divine the matching slide (minus the extension)
  SVS=$(echo ${files} | awk -F'/' '{print $NF}' | awk -F'color-' '{print $2}')

  # Find the unmodified heatmap
  PRED=$(ls -1 ${HEAT_LOC}/prediction-${SVS}* | grep -v low_res)
  COLOR=${files}

  # Find the slide
  if [[ ! $(ls -1 ${SLIDES}/${SVS}*.$ext) ]]; then
    echo "${SLIDES}/${SVS}.XXXX.$ext does not exist."
  else
    SVS_FILE=$(ls -1 ${SLIDES}/${SVS}*.svs | head -n 1)
  fi

  if [[ -z "$SVS_FILE" ]]; then
    echo "Could not find slide."
    continue
  fi

  # Get width and height
  WIDTH=$(openslide-show-properties ${SVS_FILE} |
    grep "openslide.level\[0\].width" | awk '{print substr($2,2,length($2)-2);}')
  HEIGHT=$(openslide-show-properties ${SVS_FILE} |
    grep "openslide.level\[0\].height" | awk '{print substr($2,2,length($2)-2);}')

  # Generate CSVs and PNGs.
  python /app/src/get_grayscale_heatmaps/get_grayscale_heatmap.py ${SVS} ${WIDTH} ${HEIGHT} ${PRED} ${COLOR} ${output_dir}
done
#cp ./grayscale_heatmaps/* ${GRAYSCALE_HEATMAPS_PATH}/

exit 0
