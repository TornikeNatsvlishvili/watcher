import os

try:
    EMAIL_TO = os.environ['WATCHER_EMAIL_TO']
    EMAIL_USERNAME = os.environ['WATCHER_EMAIL_USERNAME']
except Exception:
    print('Set env vars')
    os._exit(0)