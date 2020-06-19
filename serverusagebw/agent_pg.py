"""Determine the amount of data used for the streaming."""
from os import getenv

from asyncpgsa import create_pool
from faust import App

from models import JsonData

app = App(id='serverusagebw', broker=getenv(key='KAFKA_ADDR',
                                            default='kafka://localhost'
                                            )
          )
topic = app.topic('serverusagebw', value_type=JsonData,
                  deleting=True, compacting=True)


@app.agent(topic, concurrency=1)
async def compute(records):
    """Receive message from Kafka, do the compute and print to stdout."""
    pool = await create_pool(getenv(key='PG_ADDR', default=None))
    async for record in records:
        nblisteners = record.nblisteners
        bitrate = record.bitrate
        nbdays = record.nbdays
        nbhours = record.nbhours
        total = (nbdays * nbhours * 3600 * bitrate * 1000
                 / 8 * nblisteners / 1024 / 1024)
        insert = f"insert into serverusagebw (nblisteners, bitrate, nbdays, nbhours, result) " \
                 f"VALUES ('{nblisteners}', '{bitrate}', '{nbdays}', '{nbhours}' ,'{total}');"
        await pool.execute(insert)



if __name__ == '__main__':
    app.main()
