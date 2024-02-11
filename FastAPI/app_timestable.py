from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    number: int


@app.post("/timestable")
def timestable(item: Item):
    result = {}
    for i in range (1,10):
        result[i] = item.number * i
    return {"result": result}
