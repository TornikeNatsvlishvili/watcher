import os
import logging

class Config:
    EMAIL_TO = os.environ.get('WATCHER_EMAIL_TO')
    EMAIL_USERNAME = os.environ.get('WATCHER_EMAIL_USERNAME')