from watcher.core import scan_urls
from watcher.email import Email
from watcher.settings import Config
from threading import Event
import signal
from datetime import datetime, timedelta
import logging
import sys
import json

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

def read_secrets():
    with open('/run/secrets/secrets.json') as file:
        return json.load(file)

if __name__ == "__main__":
    init_log()
    signal.signal(signal.SIGINT, signal_handler)

    logging.info('started loop')

    Config.secrets = read_secrets()
    email = Email()

    while not finished.is_set():
        next_start_date = datetime.now() - timedelta(days=1)
        magazines = scan_urls(next_start_date, stop_event=finished)
        if len(magazines) > 0:
            logging.info(f'found {len(magazines)} magazines, emailing')
            email.send_new_magazine_mail(magazines, next_start_date)
        else:
            logging.info('No new magazines')
        finished.wait(Config.SLEEP_DAYS * 24 * 60 * 60)
