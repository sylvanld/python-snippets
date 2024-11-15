from dataclasses import dataclass, field
from typing import Generic, List, Type, TypeVar
from uuid import uuid4

from snippet.config import Config, ConfigurationError


@dataclass
class RequestContextMixin:
    """Common interface between BaseRequestContext and mixins that will extend it."""

    _cache: dict = field(repr=False, init=False, default_factory=dict)

    def get(self, key):
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value


@dataclass
class BaseRequestContext(RequestContextMixin):
    """Base class that must be inherited to create app request context."""

    user_id: int = None
    is_admin: bool = False
    request_id: str = field(init=False, default_factory=lambda: uuid4().hex)


T = TypeVar("T", bound=BaseRequestContext)


class RequestContextExtension:
    def configure(self, conf: Config):
        """Implement this method if extension need to read configuration from config.

        It will only be called once and before any call to extend() is made.
        """

    def extend(self, context: BaseRequestContext):
        """Implement this method to inject additional properties in context."""


class RequestContextFactory(Generic[T]):
    """Factory class that handles extensible RequestContext instanciation."""

    conf: Config = None

    def __init__(
        self,
        request_context_class: Type[T],
        extensions: List[RequestContextExtension] = None,
    ):
        self.request_context_class = request_context_class
        self.extensions = extensions if extensions else []

    def configure(self, conf: Config):
        """Set factory config and pass it to registered extensions."""
        for extension in self.extensions:
            extension.configure(conf)
        self.conf = conf

    def make_instance(self):
        """Create a new instance of RequestContext extended by registered extensions."""
        if self.conf is None:
            raise ConfigurationError(
                "Can't create RequestContext instance before factory is configured!"
            )

        context = self.request_context_class()
        for extension in self.extensions:
            extension.extend(context)
        return context
