"""Determine the amount of data used for the streaming."""
from os import getenv

from faust import App

from models import JsonData

app = App(id='serverusagebw', broker=getenv(key='KAFKA_ADDR',
                                            default='kafka://localhost'
                                            )
          )
topic = app.topic('serverusagebw', value_type=JsonData,
                  deleting=True, compacting=True)


@app.agent(topic, concurrency=10)
async def compute(records):
    """Receive message from Kafka, do the compute and print to stdout."""
    async for record in records:
        nblisteners = record.nblisteners
        bitrate = record.bitrate
        nbdays = record.nbdays
        nbhours = record.nbhours
        print(f'"Number of listeners: {nblisteners}\n'
              f'Bitrate (kb/s): {bitrate}\n'
              f'Number of days: {nbdays} \n'
              f'Number of hours by days: {nbhours}\n'
              f'Bandwidth used (GiB): '
              f'{28125 * nbdays * nbhours * bitrate * nblisteners / 65536}"')


if __name__ == '__main__':
    app.main()
