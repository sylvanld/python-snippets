import logging
from uuid import uuid4

from snippet.logs.formatters.debug import DebugFormatter
from snippet.logs.formatters.gelf import GELFFormatter

REQUEST1_ID = uuid4().hex
REQUEST2_ID = uuid4().hex

logger = logging.getLogger("toto.log")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(GELFFormatter())
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)


logger.info(
    "%(http_method)s %(http_path)s",
    extra={
        "africa": "yolo",
        "http_status": 200,
        "http_method": "GET",
        "http_endpoint": "/accounts/{accountId}",
        "http_path": "/accounts/fe8z4f8ez4f8ez",
        "request_id": REQUEST1_ID,
    },
)


logger.info(
    "POST /accounts",
    extra={
        "http_status": 409,
        "http_method": "POST",
        "http_endpoint": "/accounts",
        "http_path": "/accounts",
        "request_id": REQUEST2_ID,
    },
)


logger.warning(
    "Cannot create account. An account already exists with email: %(account_email)s",
    extra={"account_email": "toto@example.com"},
)
