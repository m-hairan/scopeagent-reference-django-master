import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def ping(request):
    logger.debug("received request for ping view", extra={'request': request})
    return HttpResponse("pong")


def ping_test():
    logger.debug("received testing request for ping view")
    response = ping(None)
    return response.status_code, response.content
