# streaming_calc_faust
Bandwidth calculation for streaming server - webservice | Rewrite from my original in Python

## Needed
- Python 3.6+
- [Kafka](https://kafka.apache.org/) (running on localhost)
- [Faust](https://github.com/robinhood/faust)
- [kafka-python](https://github.com/dpkp/kafka-python)

## Workflow

### Inject test data

Replace 50 by the number that you want in each topic.

```
python inject.py 50
```

### Start worker
```
python bwserver.py -L uvloop worker -l info -p 9001
python serverusagebw.py -L uvloop worker -l info -p 9002
```