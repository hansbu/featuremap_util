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

### BUILD AND RUN

```
./do.sh /path/to/input/dir /path/to/output/dir /path/to/svs/dir
```

### CSV to JSON

```
docker exec jsonic csv_to_json
```