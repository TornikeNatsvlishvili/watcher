from watcher.core import scan_urls
from watcher.email import Email
from watcher.settings import Config
from threading import Event
import signal
from datetime import datetime
import logging
import sys

finished = Event()


def signal_handler(signum, frame):
    logging.info('...stopping')
    finished.set()


def init_log():
    if Config.DEBUG:
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


if __name__ == "__main__":
    init_log()
    signal.signal(signal.SIGINT, signal_handler)

    logging.info('started loop')

    email = Email()
    # next_start_date = datetime.now()
    next_start_date = datetime(year=2017, month=11, day=1)
    while not finished.is_set():
        magazines = scan_urls(next_start_date)
        if len(magazines) > 0:
            logging.info(f'found {len(magazines)} magazines, emailing')
            email.send_new_magazine_mail(magazines, next_start_date)
        else:
            logging.info('No new magazines')
        finished.wait(Config.SLEEP)
