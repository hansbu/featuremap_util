### Build and run

```
./build.sh /path/to/input/dir /path/to/output/dir /path/to/wsi/dir
```

Input files go in input directory!<br>
Program will output files to the output folder you specified!


### Prediction files to featuremap
Let's say you have a bunch of prediction files (color-\*, prediction-\*) and you want to genereate featuremaps.  Run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
nohup docker exec quip-maputil pred_to_map [svs | tif | ext] &
```


### Prediction file merge
**Merge TIL & Cancer prediction**
We've got TIL predictions and cancer predictions.  Here's what to do.  Run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
cd input; mkdir til cancer
# put input files in input/til and input/cancer
# then run
nohup docker exec quip-maputil merge_cancer_til [svs | tif | ext] &
```


### Pyradiomics to featuremap
We've generated a bunch of pyradiomics csv files.  Here's how to create featuremaps:

```
docker exec quip-maputil pyrad_to_map
```
