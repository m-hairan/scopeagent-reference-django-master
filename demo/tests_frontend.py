import logging
import os
from unittest import skipUnless

import codescope
import requests
from django.test import TestCase

from demo.views import ping_test, sync_hash_test

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

    def test_sync_hash_unit(self):
        logger.info("testing sync_hash by using Django client")
        response = self.client.get('/api/hash/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")

    @skipUnless(os.getenv('CI') is not None, "not in CI")
    def test_ping_integration(self):
        logger.info("testing ping by sending request to a frontend in a CI environment")
        response = requests.get('http://%s/ping' % self.live_host)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"pong")

    @skipUnless(os.getenv('CI') is not None, "not in CI")
    def test_sync_task_integration(self):
        logger.info("testing sync_task by sending request to a frontend in a CI environment")
        response = requests.get('http://%s/api/hash/test' % self.live_host)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")


class LiveTests(codescope.testing.TestCase):
    def test_ping(self):
        logger.info("testing ping by direct remote function call to a frontend in a live environment")
        status_code, content = ping_test()
        self.assertEqual(status_code, 200)
        self.assertEqual(content, b"pong")

    def test_sync_task(self):
        logger.info("testing sync_task by sending request to a frontend in a live environment")
        status_code, content = sync_hash_test("test")
        self.assertEqual(status_code, 200)
        self.assertEqual(content, b"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")
