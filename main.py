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
    """Return API metadata and planned endpoints."""
    return {"name" : "Fly Rank CRUD API",
            "version" : "1.0",
            "endpoints" : ["/tasks","/health"]}

@app.get("/health")   
def API_Health():
    """Check the health status of the application server."""
    return {"status" : "ok"}

@app.get("/tasks")
def get_all_tasks(done: bool | None = None, search: str | None = None):
    """Retrieve tasks with optional filters for completion status and title search."""
    results = in_memoryDB
    
    # Filter by query parameter: ?done=true or ?done=false
    if done is not None:
        results = [task for task in results if task["done"] == done]
        
    # Search by query parameter: ?search=milk
    if search:
        results = [task for task in results if search.lower() in task["title"].lower()]
        
    return results

@app.get("/tasks/{id}")
def get_tasks(id:int):
    """Retrieve details for a single task using its unique integer ID."""
    for i in in_memoryDB:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

from fastapi import Body, HTTPException

@app.post("/tasks", status_code=201)
def create_task(payload: dict = Body(...)):
    """Create a new task with a unique sequential ID and default 'done' status to False."""
    
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

@app.put("/tasks/{id}")
def update_tasks(id:int, payload: dict = Body(...)):
    """Modify the title and/or completion status of an existing task."""
    target_task = None
    for task in in_memoryDB:
        if task["id"] == id:
            target_task = task
            break
        
    if target_task is None:
        raise HTTPException(status_code=404, detail=f"Task {id} Not Found")
    
    has_title = "title" in payload
    has_done = "done" in payload
    
    if not has_title and not has_done:
        raise HTTPException(status_code=400, detail="Must provide 'title' or 'done' to update")
        
    if has_title and (not isinstance(payload["title"], str) or not payload["title"].strip()):
        raise HTTPException(status_code=400, detail="Title must be a non-empty string")
        
    if has_done and not isinstance(payload["done"], bool):
        raise HTTPException(status_code=400, detail="Done must be a boolean (true/false)")

   
    if has_title:
        target_task["title"] = payload["title"].strip()
    if has_done:
        target_task["done"] = payload["done"]
        
    return target_task


@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    """Remove a task from the database permanently."""
    for index, task in enumerate(in_memoryDB):
        if task["id"] == id:
            in_memoryDB.pop(index)
            return
            
    # Unknown id → 404
    raise HTTPException(status_code=404, detail=f"Task {id} not found")
    
@app.get("/stats")
def get_api_stats():
    """Compute live real-time statistics of all tasks in memory."""
    total_tasks = len(in_memoryDB)
    done_tasks = sum(1 for task in in_memoryDB if task["done"])
    open_tasks = total_tasks - done_tasks
    
    return {
        "total": total_tasks,
        "done": done_tasks,
        "open": open_tasks
    }

    

