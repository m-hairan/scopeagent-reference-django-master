import logging

import codescope
from django.http import HttpResponse


logger = logging.getLogger(__name__)


@codescope.register()
def ping(request):
    logger.debug("received request for ping view", extra={'request': request})
    return HttpResponse("pong")
