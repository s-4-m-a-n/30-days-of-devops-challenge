from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis.asyncio as redis
import os

app = FastAPI()

redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), db=0)

class KeyValue(BaseModel):
    key: str
    value: str


@app.get("/ping")
async def health_check():
    return {"message": "pong"}


@app.put("/store")
async def store_key_value(item: KeyValue):
    try:
        await redis_client.set(item.key, item.value)
        return {"message": f"Stored {item.key}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/store/{key}")
async def get_value(key: str):
    try:
        value = await redis_client.get(key)
        if value is None:
            raise HTTPException(status_code=404, detail="Key not found")
        return {"key": key, "value": value.decode("utf-8")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))