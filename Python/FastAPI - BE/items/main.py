from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str
    is_done: bool = False


items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_items(item: Item):  # Query params
    items.append(item)
    return items


@app.get("/items")
def get_items():
    return items


@app.get("items/{item_id}")
def get_item_by_id(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item {item_id} not found.")


@app.delete("/items", response_model=list[Item])
def delete_items(item: Item):
    items.remove(item)
    return items
