from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def usaib():
    return {"name" : "Fly Rank CRUD API",
            "version" : "1.0",
            "endpoints" : ["/tasks","/health"]}

@app.get("/health")   
def API_Health():
    return {"status" : "ok"}