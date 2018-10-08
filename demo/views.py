import logging

import codescope
from django.http import HttpResponse

from demo import tasks

logger = logging.getLogger(__name__)


def ping(request):
    logger.debug("received request for ping view", extra={'request': request})
    return HttpResponse("pong")


def sync_hash(request, value):
    logger.debug("received request for sync_hash view", extra={'request': request})
    return HttpResponse(tasks.slow_hash.delay(value).get(timeout=10))


@codescope.register()
def ping_test():
    logger.debug("received testing request for ping view")
    response = ping(None)
    return response.status_code, response.content


@codescope.register()
def sync_hash_test(value):
    logger.debug("received testing request for sync_hash view")
    response = sync_hash(None, value)
    return response.status_code, response.content
