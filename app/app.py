from app.core import scan_urls
from app.email import Email

from threading import Event
from datetime import datetime
import logging

finished = Event()

SLEEP = 24 * 60 * 60  # every 24 hours

def loop():
    logging.info('started loop')
    email = Email()
    next_start_date = datetime.now()
    # next_start_date = datetime(year=2017, month=11, day=1)
    while not finished.is_set():
        
        magazines = scan_urls(next_start_date)
        if len(magazines) > 0:
            logging.info(f'found {len(magazines)} magazines, emailing')    
            email.send_new_magazine_mail(magazines, next_start_date)
        else:
            logging.info(f'No new magazines')
        finished.wait(SLEEP)
        next_start_date = datetime.now()
