import logging

import codescope
from django.http import HttpResponse
from django.test import Client

logger = logging.getLogger(__name__)


def ping(request):
    logger.debug("received request for ping view", extra={'request': request})
    return HttpResponse("pong")


@codescope.register()
def remote_test_client(method, *args, **kwargs):
    client = Client()
    response = getattr(client, method)(*args, **kwargs)
    return response.status_code, response.content
