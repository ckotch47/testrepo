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


@app.get('/auto')
async def return_message():
    return '<h1>this autodeploy</h1>'


@app.get('/auto-test')
async def return_message():
    return '<h1>this autodeploy test</h1>'


@app.get('/auto-test-1')
async def return_message():
    return '<h1>this autodeploy test123</h1>'

@app.get('/auto-test-2')
async def return_message():
    return '<h1>this autodeploy test -2 </h1>'

@app.get('/auto-test-3')
async def return_message():
    return '<h1>this autodeploy test -3 </h1>'