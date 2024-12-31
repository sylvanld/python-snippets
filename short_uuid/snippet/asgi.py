from typing import List

import fastapi
from pydantic import BaseModel, Field

from snippet.short_uuid import ShortUUID

app = fastapi.FastAPI(docs_url="/")


class IntrospectPayloadV2(BaseModel):
    short_uuid: ShortUUID = Field(alias="shortUUID")


class GenerateShortUUIDsPayloadV2(BaseModel):
    count: int


def introspect(short_uuid: ShortUUID):
    return {"uuid": short_uuid.uuid, "shortUUID": short_uuid}


@app.get("/v1/short-uuid/introspect/{shortUUID}")
async def introspect_short_uuid_v1(
    short_uuid: ShortUUID = fastapi.Path(alias="shortUUID"),
):
    return introspect(short_uuid)


@app.post("/v2/short-uuid/introspect")
async def introspect_short_uuid_v2(payload: IntrospectPayloadV2):
    return introspect(payload.short_uuid)


@app.post("/v2/short-uuid/generate", response_model=List[ShortUUID])
async def generate_short_uuids_v2(payload: GenerateShortUUIDsPayloadV2):
    return [ShortUUID.generate() for _ in range(payload.count)]
