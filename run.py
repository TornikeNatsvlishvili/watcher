from app.app import loop, finished

import click
import signal
from threading import Thread
import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M',
                    filename='/tmp/magazine_dl.log',
                    filemode='w')

def signal_handler(signum, frame):
    print('...stopping')
    finished.set()


def init_signals():
    signal.signal(signal.SIGINT, signal_handler)


@click.group()
def cli():
    pass


@cli.command()
def start():
    init_signals()
    t = Thread(target=loop)
    t.start()
    t.join()


if __name__ == '__main__':
    cli()
