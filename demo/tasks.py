import hashlib
import logging
import time

import codescope

from demo.celery import app

logger = logging.getLogger(__name__)


@app.task
def ping():
    logger.debug("received request for ping task")
    return "pong"


@app.task
def slow_hash(value):
    logger.debug("received request for slow_hash task")
    time.sleep(0.2)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


@codescope.register()
def ping_test():
    logger.debug("received testing request for ping task")
    return ping()
