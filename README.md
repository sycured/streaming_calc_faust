# streaming_calc_faust
Bandwidth calculation for streaming server - webservice | Rewrite from my original in Python

## Needed
- Python 3.6+
- Kafka (running on localhost)
- Faust

## Workflow

### Inject test data

```
./inject.sh
```

### Start worker
```
faust -L uvloop -A bwserver worker -l info -p 9001
faust -L uvloop -A serverusagebw worker -l info -p 9002
```