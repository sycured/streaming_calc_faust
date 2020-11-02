"""Determine necessary server bandwidth."""
from os import getenv

from faust import App

from models import JsonData

app = App(id='bwserver', broker=getenv(key='KAFKA_ADDR',
                                       default='kafka://localhost'
                                       )
          )
topic = app.topic('bwserver', value_type=JsonData,
                  deleting=True, compacting=True)


@app.agent(topic, concurrency=10)
async def compute(records):
    """Receive message from Kafka, do the compute and print to stdout."""
    async for record in records:
        nblisteners = record.nblisteners
        bitrate = record.bitrate
        total = 125 * nblisteners * bitrate / 128
        print(f'Number of listeners: {nblisteners}\nBitrate (kb/s): {bitrate}'
              f'\nServer bandwidth (Mib/s): {total}')


if __name__ == '__main__':
    app.main()
