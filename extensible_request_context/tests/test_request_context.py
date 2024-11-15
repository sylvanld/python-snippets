import unittest

from snippet.config import Config
from snippet.context import (
    BaseRequestContext,
    ConfigurationError,
    RequestContextFactory,
)
from tests.fakes import FakeContextExtension, FakeRequestContext


class TestRequestContext(unittest.TestCase):
    def test_factory_with_base_request_context(self):
        conf = Config(database_url="fake_database_url")
        factory = RequestContextFactory(BaseRequestContext)
        factory.configure(conf)

        context = factory.make_instance()

        self.assertIsInstance(context, BaseRequestContext)
        self.assertIsNotNone(context.request_id)
        self.assertEqual(context.is_admin, False)

    def test_factory_with_base_request_context_not_configured(self):
        factory = RequestContextFactory(BaseRequestContext)
        self.assertRaises(ConfigurationError, factory.make_instance)

    def test_factory_with_extended_request_context(self):
        conf = Config(database_url="fake_database_url")
        factory = RequestContextFactory(
            FakeRequestContext, extensions=[FakeContextExtension()]
        )
        factory.configure(conf)

        context = factory.make_instance()

        self.assertIsInstance(context, FakeRequestContext)
        self.assertIsNotNone(context.request_id)
        self.assertEqual(context.is_admin, False)
        self.assertEqual(context.get_database_url(), "fake_database_url")
