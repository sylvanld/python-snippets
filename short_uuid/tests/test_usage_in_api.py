import unittest

from fastapi.testclient import TestClient

from snippet.asgi import app
from snippet.short_uuid import ShortUUID

TEST_SHORT_UUID = "49DzG8iHwugcGbYYHOlF5i"
TEST_EQUIV_UUID = "88890581-f040-4387-92d4-16dd908e0904"


class TestUsageInAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_short_uuid_path_parameter(self):
        response = self.client.get(f"/v1/short-uuid/introspect/{TEST_SHORT_UUID}")
        assert response.status_code == 200
        assert response.json() == {
            "uuid": "88890581-f040-4387-92d4-16dd908e0904",
            "shortUUID": "49DzG8iHwugcGbYYHOlF5i",
        }

    def test_short_uuid_body_parameter(self):
        response = self.client.post(
            "/v2/short-uuid/introspect", json={"shortUUID": TEST_SHORT_UUID}
        )
        assert response.status_code == 200
        assert response.json() == {
            "uuid": "88890581-f040-4387-92d4-16dd908e0904",
            "shortUUID": "49DzG8iHwugcGbYYHOlF5i",
        }

    def test_short_uuid_serialization(self):
        response = self.client.post("/v2/short-uuid/generate", json={"count": 3})
        assert response.status_code == 200

        output_short_uuids = response.json()
        assert len(output_short_uuids) == 3

        for short_uuid_string in output_short_uuids:
            short_uuid = ShortUUID(short_uuid_string)
            assert isinstance(short_uuid, ShortUUID)
