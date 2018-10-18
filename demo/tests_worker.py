import logging
import os
from unittest import skipUnless

from django.test import TestCase

from demo.tasks import ping, slow_hash

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


class UnitTests(TestCase):
    def test_ping_unit(self):
        logger.info("testing ping by direct function call")
        self.assertEqual(ping(), "pong")

    def test_slow_hash_unit(self):
        logger.info("testing slow_hash by direct function call")
        self.assertEqual(slow_hash("test"), "bc89c6f72947bcd2f783d342a46cafcfccfcc2e7884a34f1cfe8f55bad2d200e")

    @skipUnless(os.getenv('CI') is not None, "not in CI")
    def test_ping_integration(self):
        logger.info("testing ping by sending task to a worker in a CI environment")
        self.assertEqual(ping.delay().get(timeout=10), "pong")

    @skipUnless(os.getenv('CI') is not None, "not in CI")
    def test_slow_hash_integration(self):
        logger.info("testing slow_hash by sending task to a worker in a CI environment")
        self.assertEqual(slow_hash.delay("test").get(timeout=10),
                         "bc89c6f72947bcd2f783d342a46cafcfccfcc2e7884a34f1cfe8f55bad2d200e")
