""" Module for Fast Api operations. """
# Using serve approach from online
import asyncio
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel #type : ignore
import uvicorn


class Gadget(BaseModel):
    """Gadget Model class """
    id: int
    name: str
    price:float

# app = FastAPI()

# @app.get("/")
class ApiController:
    """Api Controller class """
    app : FastAPI

    def __init__(self) -> None:
        self.app = FastAPI()

    async def serve(self):
        """Fast API Serve """
        app: FastAPI = self.app

        @app.get("/")
        async def read()-> dict[str, str | int]: #type : ignore
            """Read root """
            return  {"name": "Default Gadget", "id": 1}

        @app.get("/gadgets/{gadget_id}")
        async def read_gadget(gadget_id: int,
                            input_qry: Union[str, None]=None) -> dict[str, str | int]:
            """Read gadgets """
            return {"gadget_id": gadget_id, "q": input_qry} # type: ignore

        @app.post("/gadgets/{gadget_id}")
        async def write_gadget(gadget_id: int, gadget: Gadget) -> dict[str, Gadget | int]:
            """Write Gadget"""
            return {"Gadget": gadget, "gadget_id": gadget_id}

        @app.put("/gadgets/{gadget_id}")
        async def update_gadget(gadget_id: int, gadget: Gadget) -> dict[str, str | float]:
            """Update Gadget"""
            return {"name": gadget.name, "price": gadget.price, "id": gadget_id}


        uvicorn_config =  uvicorn.Config(app, host='localhost',port=8080)
        uvicorn_server =  uvicorn.Server(uvicorn_config)
        await uvicorn_server.serve()

# application would run at localhost using port 8080
if __name__ == "__main__":
    controller = ApiController()
    asyncio.run(controller.serve())
