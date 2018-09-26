import logging
import time
import unittest

import codescope
import opentracing
import requests

from demo.tasks import hello_world

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


class UnitTests(unittest.TestCase):
    def test_hello_world(self):
        logger.info("hello world!")
        self.assertEqual(hello_world(), "hello world!")

    def test_with_spans(self):
        logger.info("starting test")
        with opentracing.tracer.start_active_span('first_step', finish_on_close=True):
            logger.info("starting first step")
            time.sleep(0.5)
            logger.info("finishing first step")
        time.sleep(0.2)
        with opentracing.tracer.start_active_span('second_step', finish_on_close=True):
            logger.info("starting second step")
            with opentracing.tracer.start_active_span('first_substep', finish_on_close=True):
                logger.info("starting second step first substep")
                time.sleep(0.5)
                logger.info("finishing second step first substep")
            time.sleep(0.5)
            logger.info("finishing second step")

    def test_with_http_request(self):
        r = requests.get('https://ifconfig.co')
        r.raise_for_status()


class LiveTests(codescope.testing.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world!")
