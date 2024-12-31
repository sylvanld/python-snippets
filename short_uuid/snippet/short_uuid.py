from string import ascii_lowercase, ascii_uppercase, digits
from typing import Union
from uuid import UUID, uuid4


class ShortUUID(str):
    """Pydantic compatible, compact UUID format."""

    symbols = digits + ascii_lowercase + ascii_uppercase

    def __init__(self, value: Union[str, "ShortUUID"]):
        if isinstance(value, str) or isinstance(value, ShortUUID):
            self.value = str(value)
            self.uuid = UUID(int=self._short_uuid_to_int(self.value))
        else:
            raise ValueError("ShortUUID value must be a string")

    def _short_uuid_to_int(self, short_uuid: str) -> bytes:
        value = 0
        N = len(short_uuid)
        C = len(self.symbols)
        for k in range(N):
            digit = self.symbols.index(short_uuid[k])
            base = C ** (N - k - 1)
            value += base * digit
        return value

    @staticmethod
    def from_uuid(uuid: UUID):
        x = int(uuid.int)
        C = len(ShortUUID.symbols)
        value = ""
        while x > 0:
            q = x // C
            r = x - C * q
            value = ShortUUID.symbols[r] + value
            x = q
        return ShortUUID(value)

    @staticmethod
    def generate():
        return ShortUUID.from_uuid(uuid4())

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        from pydantic_core import core_schema

        core_schema.SerSchema

        return core_schema.no_info_after_validator_function(
            cls, core_schema.any_schema()
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = handler(core_schema)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema["example"] = "49DzG8iHwugcGbYYHOlF5i"
        json_schema["format"] = "ShortUUID"
        return json_schema
