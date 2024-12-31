import unittest
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from snippet.short_uuid import ShortUUID

TEST_SHORT_UUID = "49DzG8iHwugcGbYYHOlF5i"
TEST_EQUIV_UUID = UUID("88890581-f040-4387-92d4-16dd908e0904")


class TestShortUUID(unittest.TestCase):
    def test_short_uuid_equivalence(self):
        uuid = ShortUUID(TEST_SHORT_UUID)
        self.assertEqual(uuid.uuid, TEST_EQUIV_UUID)

    def test_short_uuid_string_conversion(self):
        uuid = ShortUUID(TEST_SHORT_UUID)
        self.assertEqual(str(uuid), TEST_SHORT_UUID)

    def test_short_uuid_random_generation(self):
        uuid = ShortUUID.generate()
        self.assertIsInstance(uuid.uuid, UUID)

    def test_short_uuid_pydantic_deserialization(self):
        class TestModel(BaseModel):
            short_uuid: ShortUUID = Field(alias="shortUUID")

        data = TestModel.model_validate({"shortUUID": TEST_SHORT_UUID})
        self.assertIsInstance(data.short_uuid, ShortUUID)
        self.assertEqual(data.short_uuid.uuid, TEST_EQUIV_UUID)

    def test_short_uuid_pydantic_serialization(self):
        class TestModel(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            short_uuid: ShortUUID = Field(alias="shortUUID")

        short_uuid = ShortUUID(TEST_SHORT_UUID)
        data = TestModel(short_uuid=short_uuid)
        output = data.model_dump(by_alias=True)
        self.assertEqual(output, {"shortUUID": TEST_SHORT_UUID})
