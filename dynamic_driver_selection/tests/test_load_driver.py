import os
import unittest

from snippet.config import Config


class TestLoadDriver(unittest.TestCase):
    def test_load_existing_implementation(self):
        os.environ["FOO"] = "bar"
        config = Config.create("environment")
        value = config.get("foo")
        self.assertEqual("bar", value)

    def test_load_undefined_implementation(self):
        self.assertRaises(ValueError, Config.create, "undefined")
