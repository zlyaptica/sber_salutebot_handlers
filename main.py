from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/documents")
async def search_data(item: Item):
    print(item)
    return JSONResponse({"text": item.dict()})

@app.get("/")
async def homepage():
    return JSONResponse({'hello': 'world'})