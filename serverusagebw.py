"""Determine the amount of data used for the streaming."""
from faust import App, Record


class JsonData(Record):
    """Json schema from Kafka."""

    nblisteners: float
    bitrate: float
    nbdays: float
    nbhours: float


app = App(id='serverusagebw', broker='kafka://localhost')
topic = app.topic('serverusagebw', value_type=JsonData)


@app.agent(topic)
async def compute(records):
    """Receive message from Kafka, do the compute and print to stdout."""
    async for record in records:
        nblisteners = record.nblisteners
        bitrate = record.bitrate
        nbdays = record.nbdays
        nbhours = record.nbhours
        total = (nbdays * nbhours * 3600 * bitrate * 1000
                 / 8 * nblisteners / 1024 / 1024)
        print(f'"Number of listeners: {nblisteners}\n'
              f'Bitrate (kb/s): {bitrate}\n'
              f'Number of days: {nbdays} \n'
              f'Number of hours by days: {nbhours}\n'
              f'Bandwidth used (GiB): {total}"')
