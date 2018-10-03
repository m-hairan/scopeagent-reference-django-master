import logging

import codescope

from demo.celery import app

logger = logging.getLogger(__name__)


@app.task
def ping():
    logger.debug("received request for ping task")
    return "pong"


@codescope.register()
def ping_test():
    logger.debug("received testing request for ping task")
    return ping()
