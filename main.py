from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

in_memoryDB = [
    {"id":1, "title":"Create Task", "done": True},
    {"id":2, "title":"Update Task", "done": False},
    {"id":3, "title":"Delete Task", "done": True}
]

@app.get("/")
async def usaib():
    return {"name" : "Fly Rank CRUD API",
            "version" : "1.0",
            "endpoints" : ["/tasks","/health"]}

@app.get("/health")   
def API_Health():
    return {"status" : "ok"}

@app.get("/tasks")
def get_all_tasks():
    return in_memoryDB

@app.get("/tasks/{id}")
def get_tasks(id:int):
    for i in in_memoryDB:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

from fastapi import Body, HTTPException

@app.post("/tasks", status_code=201)
def create_task(payload: dict = Body(...)):
    
    if "title" not in payload or not isinstance(payload["title"], str) or not payload["title"].strip():
        raise HTTPException(status_code=400, detail="Title is required and cannot be empty")
        
    
    next_id = max([task["id"] for task in in_memoryDB], default=0) + 1
    
    
    new_task = {
        "id": next_id,
        "title": payload["title"].strip(),
        "done": False
    }
    in_memoryDB.append(new_task)
    
    return new_task


