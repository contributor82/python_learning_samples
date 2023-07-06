from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_items(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q": q}



# uvicorn main:app

# application would run at localhost using port 8080
if __name__ == "__main__": 
    uvicorn.run(app,port=8080,host='127.0.0.1')

