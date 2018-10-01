import logging

import codescope

from demo.celery import app

logger = logging.getLogger(__name__)


@app.task
@codescope.register()
def ping():
    return "pong"
