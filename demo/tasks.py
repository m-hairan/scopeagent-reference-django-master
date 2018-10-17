import hashlib
import logging
import time

import opentracing

from demo.celery import app

logger = logging.getLogger(__name__)


@app.task
def ping():
    logger.debug("received request for ping task")
    return "pong"


@app.task
def slow_hash(value):
    logger.debug("received request for slow_hash task")
    loops = 0
    while loops < 10:
        with opentracing.tracer.start_active_span("slow_hash.hash") as scope:
            scope.span.set_tag('loop', loops)
            value = hashlib.sha256(value.encode('utf-8')).hexdigest()
            time.sleep(0.1)
            logger.info("calculated intermediate hash: %s", value, extra={'value': value})
            loops += 1
    logger.info("calculated final hash: %s", value, extra={'value': value})
    return value
