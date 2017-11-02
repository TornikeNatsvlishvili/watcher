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
    while not finished.is_set():
        start_date = datetime.now()
        # start_date = datetime(year=2017, month=10, day=29)
        
        magazines = scan_urls(start_date)
        if len(magazines) > 0:
            logging.info(f'found {len(magazines)} magazines, emailing')    
            email.send_new_magazine_mail(magazines, start_date)
        else:
            logging.info(f'No new magazines')
        finished.wait(SLEEP)
