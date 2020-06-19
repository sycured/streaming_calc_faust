"""Create tables inside postgresql."""
from asyncio import run
from os import getenv

from asyncpgsa import create_pool

from uvloop import install as uvloop_install


async def main():
    """Connect to postgresql and execute queries to create tables."""
    bwserver_table = 'create table bwserver(nblisteners float, ' \
                     'bitrate float, result float);'

    serverusagebw_table = 'create table serverusagebw(nblisteners float, ' \
                          'bitrate float, nbdays float, nbhours float, ' \
                          'result float);'

    pool = await create_pool(getenv(key='PG_ADDR', default=None))
    await pool.execute(bwserver_table)
    await pool.execute(serverusagebw_table)
    await pool.close()


if __name__ == '__main__':
    uvloop_install()
    run(main())
