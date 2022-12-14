"""
    fastapi - using pip install fastapi.
    uvicorn for start server - using pip install uvicorn
    in terminal uvicorn main:app
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """

    :return: strung
    """
    return {"message": "Hello World"}
