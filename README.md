## Featuremap Utility
Generate featuremaps.  Most of the time you'll be converting prediction files to featuremap files.
Or, you may want to generate a featuremap from a spreadsheet containing pyradiomics data.

### Build and run

```
./build.sh /path/to/input/dir /path/to/output/dir /path/to/wsi/dir
```

Input files go in input directory!<br>
Program will output files to the output folder you specified!
<br>


## Usage

### Prediction files to featuremap
Let's say you have a bunch of prediction files (color-\*, prediction-\*) and you want to generate featuremaps.  Run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
nohup docker exec quip-maputil pred_to_map [svs | tif | ext] &
```
<br>


### Prediction file merge
**Merge TIL & Cancer prediction**
We've got TIL predictions and cancer predictions.  Here's what to do.  Run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
cd input; mkdir til cancer
# put input files in input/til and input/cancer
# then run
nohup docker exec quip-maputil merge_cancer_til [svs | tif | ext] &
```
<br>


### Pyradiomics to featuremap
We've generated a bunch of pyradiomics csv files.  Here's how to create featuremaps:

```
docker exec quip-maputil pyrad_to_map
```
<br>


<a href="https://github.com/SBU-BMI/featuremap_util/blob/master/README1.md" target="_blank">View</a> other, less frequently used functions.
