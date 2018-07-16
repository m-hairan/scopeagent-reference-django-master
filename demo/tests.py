from codescope.testing import CodescopeTestCase

from demo.tasks import hello_world


# class UnitTests(unittest.TestCase):
#     def test_pass(self):
#         pass
#
#     def test_fail(self):
#         self.fail("fail")
#
#     def test_skip(self):
#         self.skipTest("skip")
#
#     def test_error(self):
#         raise Exception("test exception")
#
#     def test_celery(self):
#         from .celery import debug_task
#         r = debug_task.delay()
#         print(r.get())
#
#     def test_local(self):
#         self.assertEqual(mine_block(base64.b64encode(b"test").decode('utf-8'), 1), 48)


class LiveTests(CodescopeTestCase):
    def test_live(self):
        self.assertEqual(hello_world(), "hello world!")
