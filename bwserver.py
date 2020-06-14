"""Determine necessary server bandwidth."""
from faust import App, Record


class JsonData(Record):
    """Json schema from Kafka."""

    nblisteners: float
    bitrate: float


app = App(id='bwserver', broker='kafka://localhost')
topic = app.topic('bwserver', value_type=JsonData)


@app.agent(topic, concurrency=10)
async def compute(records):
    """Receive message from Kafka, do the compute and print to stdout."""
    async for record in records:
        nblisteners = record.nblisteners
        bitrate = record.bitrate
        total = nblisteners * bitrate * 1000 / 1024
        print(f'Number of listeners: {nblisteners}\nBitrate (kb/s): {bitrate}'
              f'\nServer bandwidth (Mib/s): {total}')
