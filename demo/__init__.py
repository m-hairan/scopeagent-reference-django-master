from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
import codescope
from django.test import Client

from .celery import app as celery_app

__all__ = ('celery_app', 'remote_test_client',)


@codescope.register()
def remote_test_client(method, *args, **kwargs):
    client = Client()
    response = getattr(client, method)(*args, **kwargs)
    return response.status_code, response.content
