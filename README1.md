## Usage, cont'd.

### PNG to featuremap
Let's say we don't have the prediction files, but we have a bunch of PNGs.  Here's how to generate featuremaps.  Again, run the following command, substitute `[svs | tif | ext]` with the file extension of the slide.

```
docker exec quip-maputil png_to_map [svs | tif | ext]
```


<br>
### CSV to featuremap
The FeatureMap application accepts data in JSON format.  Let's say we have a "legacy" map, i.e. one with a JSON "header", and then columns `i, j, R, G, B`.  And we want to convert them to proper featuremaps.  Here's how:

```
docker exec quip-maputil csv_to_json
```
<br>



<!--
<hr>

## Output data format
The output data format is in JSON.

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



<!--
### Build

```
docker build -t featuremap_util .
```

### Run
```
docker run --name quip-maputil -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output -itd featuremap_util

./build.sh $(pwd)/input $(pwd)/output /path/to/wsi/dir

```
-->
