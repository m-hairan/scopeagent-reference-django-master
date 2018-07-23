from codescope.testing import TestCase

from demo.tasks import hello_world


class LiveTests(TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world!")
