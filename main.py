from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def usaib():
    return {"message": "Hello World"}