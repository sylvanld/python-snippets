import unittest

from snippet.foo import get_foo


class TestFoo(unittest.TestCase):
    def test_foo_exists(self):
        value = get_foo(should_fail=False)
        self.assertIsNotNone(value)

    def test_handle_foo_failure(self):
        self.assertRaises(ValueError, get_foo, should_fail=True)
