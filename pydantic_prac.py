from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    # item_dict = item.model_dump()
    # if item.tax is not None:
    #     item_dict.update({"price_with_tax":item.price + item.tax})
    # return item_dict
    return item

class InvestigationRequest(BaseModel):
    input: str

@app.post("/investigation/")
async def investigate(input: InvestigationRequest):
    return input