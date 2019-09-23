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

```
docker exec quip-maputil pred_to_map
```

### PNG to featuremap

```
docker exec quip-maputil png_to_map
```

### Pyradiomics to featuremap

```
docker exec quip-maputil pyrad_to_map
```

<!--
### CSV to JSON

```
docker exec quip-maputil csv_to_map
```
-->
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