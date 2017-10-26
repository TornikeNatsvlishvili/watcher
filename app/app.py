from app.core import scan_urls
from app.email import send_new_magazine_mail

from threading import Event
from datetime import datetime
import logging

finished = Event()

SLEEP = 60 * 60  # every hour

def loop():
    while not finished.is_set():
        start_date = datetime.now()
        
        magazines = scan_urls(start_date)
        if len(magazines) > 0:
            send_new_magazine_mail(magazines, start_date)
        else:
            logging.info(f'No new magazines')
        finished.wait(SLEEP)
