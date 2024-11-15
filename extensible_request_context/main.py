from snippet.config import CONF
from snippet.context import BaseRequestContext, RequestContextFactory
from snippet.database import DBContextExtension, DBContextMixin


class AppRequestContext(BaseRequestContext, DBContextMixin):
    """Request content for example App that has db_session property."""

# create a factory that will inject db_session_factory for DBContextMixin
context_factory = RequestContextFactory(
    AppRequestContext, extensions=[DBContextExtension()]
)

# configure factory before calling make_instance
context_factory.configure(CONF)

# get instance of AppRequestContext
context = context_factory.make_instance()

# ensure it has access to a DB session
print(context.db_session)
