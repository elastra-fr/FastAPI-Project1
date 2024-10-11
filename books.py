from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint")
async def read_root():

    return {"message": "Hello World"}