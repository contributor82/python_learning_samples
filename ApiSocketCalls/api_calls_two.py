""" Module for Fast Api operations. """

import asyncio
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel #type : ignore
import uvicorn


class Item(BaseModel):
    """Item Model class """
    name: str
    data:list[str]

app = FastAPI()

@app.get("/")
class ApiController:
    """Api Controller class """

    @app.get("/root/")
    async def read_root(self)-> dict[str, str | int]: #type : ignore
        """Read root """
        return  {"item_name": "Default item", "item_id": 1}

    @app.get("/root/items/{item_id}")
    async def read_item(self,item_id: int,
                            input_qry: Union[str, None]=None) -> dict[str, str | int]:
        """Read Items """
        return {"item_id": item_id, "q": input_qry} # type: ignore

    @app.post("/root/items/{item_id}")
    async def write_item(self, item_id: int, item: Item) -> dict[str, Item | int]:
        """Write item"""
        return {"item": item, "item_id": item_id}

    @app.put("/root/items/{item_id}")
    async def update_item(self,item_id: int, item: Item) -> dict[str, str | list[str] | int]:
        """Update item"""
        return {"item_name": item.name, "item_data": item.data, "item_id": item_id}

    async def serve(self):
        """Fast API Serve """
        uvicorn_config =  uvicorn.Config(app, host='localhost',port=8080)
        uvicorn_server =  uvicorn.Server(uvicorn_config)
        await uvicorn_server.serve()

# application would run at localhost using port 8080
if __name__ == "__main__":
    controller = ApiController()
    asyncio.run(controller.serve())
