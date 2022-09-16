import json
import uvicorn
import uuid
from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from typing import Union

location = "assets"


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


class Dependency(BaseModel):
    name: str
    path: Union[str, None] = None
    url: Union[str, None] = None


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/dependency/")
def save_file(file: UploadFile, dependency=Form()):
    dependency_dict = json.loads(dependency)

    return {"filename": file.filename,
            "dependency": dependency_dict}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)
