## featuremap_util
<!--
### Build

```
docker build -t featuremap_util .
```

### Run
```
docker run --name quip-maputil -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output -itd featuremap_util
```-->

### Build and run

```
./build.sh /path/to/input/dir /path/to/output/dir /path/to/wsi/dir
```
<!-- ./build.sh $(pwd)/input $(pwd)/output /path/to/wsi/dir -->

Input files go in input directory!<br>
Program will output files to the output folder you specified!

### Prediction files to featuremap
Let's say you have a bunch of prediction files (color-\*, prediction-\*) and you want to genereate featuremaps.  Run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
nohup docker exec quip-maputil pred_to_map [svs | tif | ext] &
```

### PNG to featuremap
Let's say we don't have the prediction files, but we have a bunch of PNGs.  Here's how to generate featuremaps.  Again, run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
docker exec quip-maputil png_to_map [svs | tif | ext]
```

### Pyradiomics to featuremap
We've generated a bunch of pyradiomics csv files.  Here's how to create featuremaps:

```
docker exec quip-maputil pyrad_to_map
```


### CSV to featuremap
The FeatureMap application accepts data in JSON format.  Let's say we have a "legacy" map, i.e. one with a JSON "header", and then columns `i, j, R, G, B`.  And we want to convert them to proper featuremaps.  Here's how:

```
docker exec quip-maputil csv_to_json
```

### Merge TIL & Cancer to featuremap
We've got til predictions and cancer predictions.  Here's what to do.  Run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
cd input; mkdir til cancer
# put input files in input/til and input/cancer
# then run
nohup docker exec quip-maputil merge_til_tumor [svs | tif | ext] &
```


<!--
### JSON data format

```
{
    "metadata": {
        "img_width": number,
        "img_height": number,
        "png_w": number,
        "png_h": number,
        "patch_w": number,
        "patch_h": number
    },
    "data": {
        "locations": {
            "i": [list of 'i' (aka 'x' coordinates)],
            "j": [list of 'j' (aka 'y' coordinates)]
        },
        "features": {
            "TIL": [ list of feature data corresponding to i,j (see above) ],
            "Cancer": [ list of feature data corresponding to i,j (see above) ],
            "Tissue": [ list of feature data corresponding to i,j (see above) ]
        }
    }
}
```
-->
