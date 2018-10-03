import logging
import os
from unittest import skipUnless

import codescope
import requests
from django.test import TestCase

from demo import remote_test_client

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig()


class UnitTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(UnitTests, cls).setUpClass()
        cls.live_host = "%s:%s" % (os.getenv('FRONTEND_HOST', 'localhost'), os.getenv('FRONTEND_PORT', '8000'))

    def test_ping_unit(self):
        logger.info("testing ping by using Django client")
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"pong")

    @skipUnless(os.getenv('CI') is not None, "not in CI")
    def test_ping_integration(self):
        logger.info("testing ping by sending task to a frontend in a CI environment")
        response = requests.get('http://%s/ping' % self.live_host)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"pong")


class LiveTests(codescope.testing.TestCase):
    def test_ping(self):
        logger.info("testing ping by direct remote function call to a frontend in a live environment")
        status_code, content = remote_test_client('get', '/ping')
        self.assertEqual(status_code, 200)
        self.assertEqual(content, b"pong")
