import logging

import codescope

from demo.celery import app

logger = logging.getLogger(__name__)


@codescope.register()
@app.task
def ping():
    logger.debug("received request for ping task")
    return "pong"
