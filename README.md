# featuremap_util
<!--
### Build

```
docker build -t featuremap_util .
```

### Run
```
docker run --name jsonic -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output -itd featuremap_util
```-->

### Build and run

```
./build.sh /path/to/input/dir /path/to/output/dir /path/to/wsi/dir
```
<!-- ./build.sh $(pwd)/input $(pwd)/output /path/to/wsi/dir -->

### PNG to JSON

```
docker exec jsonic png_to_json
```

### Pyradiomics to featuremap

```
docker exec jsonic pyrad_to_map
```

<!--
### CSV to JSON

```
docker exec jsonic csv_to_json
```
-->

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
