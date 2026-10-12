from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html
from enum import Enum
from typing import Union
app = FastAPI(redoc_url=None)

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js",
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sum/{int1}/{int2}")
async def read_item(int1:int,int2:int):
    return {"sum":int1+int2}

class Last_name(str, Enum):
    navya = "agarwal"
    adityaa = "mehra"

@app.get("/name/{last_name}")
async def get_name(last_name: Last_name):
    if last_name == Last_name.navya:
        return {"name": "Navya"}
    if last_name.value == "mehra":
        return {"name": "Adityaa"}
    # return {"name":"not found"}

@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "maa"}, {"item_name": "mal"}, {"item_name": "tap"}]

@app.get("/items/")
async def get_items(skip: int = 0, limit: int = 6):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str,None] = None, short:bool = False):
    item = {"item_id": item_id, "user_id": "123"}
    if q and short:
        item.update({"user_id": q})
    return item

