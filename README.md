# featuremap_util

### Build

```
docker build -t featuremap_util .
```

### Run
```
docker run --name jsonic -v $(pwd)/input:/data/input -v $(pwd)/output:/data/output -itd featuremap_util
```

### CSV to JSON

```
docker exec jsonic csv_to_json
```
