from app.app import loop, finished
from app.settings import Config

import click
import signal
from threading import Thread
import os
import logging
import sys


def init_log(debug):
    if debug:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            stream=sys.stdout,
                            datefmt='%d-%m-%Y %H:%M',
                        )
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%d-%m-%Y %H:%M',
                            filename='/tmp/watcher.log',
                            filemode='w'
                        )


def signal_handler(signum, frame):
    print('...stopping')
    finished.set()


def init_signals():
    signal.signal(signal.SIGINT, signal_handler)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--debug', default=False, is_flag=True)
@click.argument('email_to')
@click.argument('email_username')
def watch(debug, email_to=None, email_username=None):
    if email_to and email_username:
        Config.EMAIL_TO = email_to
        Config.EMAIL_USERNAME = email_username
    init_log(debug)
    init_signals()
    t = Thread(target=loop)
    t.start()
    t.join()


if __name__ == '__main__':
    cli()
