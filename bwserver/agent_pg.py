"""Determine necessary server bandwidth."""
from os import getenv

from asyncpgsa import create_pool

from faust import App

from models import JsonData

app = App(id='bwserver', broker=getenv(key='KAFKA_ADDR',
                                       default='kafka://localhost'
                                       )
          )
topic = app.topic('bwserver', value_type=JsonData,
                  deleting=True, compacting=True)


@app.agent(topic, concurrency=1)
async def compute(records):
    """Receive message from Kafka, do the compute and print to stdout."""
    pool = await create_pool(getenv(key='PG_ADDR', default=None))
    async for record in records:
        nblisteners = record.nblisteners
        bitrate = record.bitrate
        total = 125 * nblisteners * bitrate / 128
        insert = f'insert into bwserver (nblisteners, bitrate, result) ' \
                 f"VALUES ('{nblisteners}', '{bitrate}', '{total}');"
        await pool.execute(insert)


if __name__ == '__main__':
    app.main()
