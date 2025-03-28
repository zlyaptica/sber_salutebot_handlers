from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/documents")
async def search_data(item: Item):
    print(item)
    return {"text": item.text}

@app.get("/")
async def homepage():
    return {'hello': 'world'}