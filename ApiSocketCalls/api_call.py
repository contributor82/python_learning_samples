from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import uvicorn


class Item(BaseModel): 
    name: str
    data:list[str]

app = FastAPI()

@app.get("/")
class ApiController():
    
     
    @app.get("/root/")
    async def read_root():
        return  {"item_name": "Default item", "item_id": 1}

    @app.get("/root/items/{item_id}")
    async def read_items(item_id: int, q: Union[str, None]=None):
        return {"item_id": item_id, "q": q}
    
    @app.post("/root/items/{item_id}")
    async def write_item(item_id: int, item: Item): 
        return {"item": Item, "item_id": item_id}
        
    @app.put("/root/items/{item_id}")
    async def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_data": item.data, "item_id": item_id}


# application would run at localhost using port 8080
if __name__ == "__main__": 
    uvicorn.run(app,port=8080,host='localhost')

