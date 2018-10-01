import logging

import codescope
from django.test import TestCase

from demo.tasks import ping

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


class UnitTests(TestCase):
    def test_ping_unit(self):
        logger.info("testing ping by direct function call")
        self.assertEqual(ping(), "pong")

    def test_ping_integration(self):
        logger.info("testing ping by sending task to live worker")
        self.assertEqual(ping.delay().get(timeout=10), "pong")


class LiveTests(codescope.testing.TestCase):
    def test_ping(self):
        self.assertEqual(ping(), "pong")
