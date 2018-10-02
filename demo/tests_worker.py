import logging
import os
from unittest import skipUnless

import codescope
from django.test import TestCase

from demo.tasks import ping

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig()


class UnitTests(TestCase):
    def test_ping_unit(self):
        logger.info("testing ping by direct function call")
        self.assertEqual(ping(), "pong")

    @skipUnless(os.getenv('CI') is not None, "not in CI")
    def test_ping_integration(self):
        logger.info("testing ping by sending task to a worker in a CI environment")
        self.assertEqual(ping.delay().get(timeout=10), "pong")


class LiveTests(codescope.testing.TestCase):
    def test_ping_live(self):
        logger.info("testing ping by direct remote function call to a worker in a live environment")
        self.assertEqual(ping(), "pong")
