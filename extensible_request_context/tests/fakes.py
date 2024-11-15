from snippet.context import (
    BaseRequestContext,
    RequestContextExtension,
    RequestContextMixin,
)

DB_URL_KEY = "database_url"


class FakeContextMixin(RequestContextMixin):
    def get_database_url(self):
        return self.get(DB_URL_KEY)


class FakeContextExtension(RequestContextExtension):
    def configure(self, conf):
        self.database_url = conf.database_url

    def extend(self, context):
        context.set(DB_URL_KEY, self.database_url)


class FakeRequestContext(BaseRequestContext, FakeContextMixin): ...
