import unittest

import codescope

from demo.tasks import hello_world


class UnitTests(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world!")


class LiveTests(codescope.testing.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world!")
