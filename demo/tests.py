import logging
import unittest

import codescope

from demo.tasks import hello_world

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


class UnitTests(unittest.TestCase):
    def test_hello_world(self):
        logger.info("hello world!")
        self.assertEqual(hello_world(), "hello world!")


class LiveTests(codescope.testing.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world!")
