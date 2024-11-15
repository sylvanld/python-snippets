from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from snippet.context import RequestContextExtension, RequestContextMixin

DB_SESSION_KEY = "db_session"
DB_SESSION_FACTORY_KEY = "db_session_factory"


class DBContextMixin(RequestContextMixin):
    """Mixin that give access to a lazy-loaded DB session in RequestContext."""

    @property
    def db_session(self) -> Session:
        session = self.get(DB_SESSION_KEY)
        if session is None:
            db_session_factory = self.get(DB_SESSION_FACTORY_KEY)
            if db_session_factory is None:
                raise ValueError("Missing db_session_factory")
            session = db_session_factory()
            self.set(DB_SESSION_KEY, session)
        return session


class DBContextExtension(RequestContextExtension):
    """Extension that creates DB session factory and pass it to context."""

    def configure(self, conf):
        self.db_session_factory = sessionmaker(bind=create_engine(conf.database_url))

    def extend(self, context):
        context.set(DB_SESSION_FACTORY_KEY, self.db_session_factory)
