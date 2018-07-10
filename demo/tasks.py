import base64
import hashlib
import logging

from demo.celery import app

logger = logging.getLogger(__name__)


@app.task
def mine_block(data, difficulty):
    data = base64.b64decode(data.encode('utf-8'))
    loops = 0
    while True:
        to_hash = b"%04X%b" % (loops, data)
        h = hashlib.sha256(hashlib.sha256(to_hash).digest()).hexdigest()
        if h.startswith('0' * difficulty):
            break
        loops += 1
    logger.info("After %d loops found hash %s (difficulty=%d)", loops, h, difficulty)
    return loops
