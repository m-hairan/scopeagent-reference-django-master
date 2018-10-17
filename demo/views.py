import logging

from django.http import HttpResponse

from demo import tasks

logger = logging.getLogger(__name__)


def ping(request):
    logger.debug("received request for ping view", extra={'request': request})
    return HttpResponse("pong")


def sync_hash(request, value):
    logger.debug("received request for sync_hash view", extra={'request': request})
    return HttpResponse(tasks.slow_hash.delay(value).get(timeout=10))
