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

#### Optional environment variable
##### for inject.py

- KAFKA_ADDR : specify url where Kafka is running and be accessible (default value: `localhost:9092`)

##### for bwserver/agent.py and serverusagebw/agent.py

- AIOKAFKA_ADDR : specify url where Kafka is running and be accessible (default value: `kafka://localhost`)

#### Standalone
```
python bwserver/agent.py -L uvloop worker -l info -p 9001
python serverusagebw/agent.py -L uvloop worker -l info -p 9002
```

#### PostgreSQL version
##### environment variable
```
PG_ADDR='postgresql://toto:titi@localhost:5432/titi'
```

##### create tables
```
python setup_db.py
```

##### start worker
```
python bwserver/agent_pg.py -L uvloop worker -l info -p 9001
python serverusagebw/agent_pg.py -L uvloop worker -l info -p 9002
```
