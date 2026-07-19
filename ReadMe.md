# 🚀 Fly Rank CRUD API

A lean, high-performance task management backend engineered with **Python** and **FastAPI**. This system demonstrates a complete in-memory transactional workflow for handling Create, Read, Update, and Delete operations.

> 💡 **Core Design Notice:** This project uses volatile, in-memory architecture. Storage resets to its base configuration during server cycles.

---

###  Technical Core
* **Runtime Environments:** Python 3.10+
* **Framework Stack:** FastAPI + Uvicorn Core Engine

```bash
# Execute environment setup dependency payload
pip install fastapi uvicorn
```

---

###  Execution Blueprint

To boot up the application gateway, dispatch the following routine inside your project root:

```bash
uvicorn main:app --reload
```

| Deployment Context | Target URL Location |
| :--- | :--- |
| **Active Live Portal** | `http://127.0.0.1:8000` |
| **Interactive Docs Panel (Swagger UI)** | `http://127.0.0.1:8000/docs` |
| **Schematic Overview Portal (ReDoc)** | `http://127.0.0.1:8000/redoc` |

---

###  Routing Interface Specification

####  System Overviews
* **`GET /`** — *Root Entrypoint.* Dispatches active system descriptor blocks.
  ```json
  { "name": "Fly Rank CRUD API", "version": "1.0", "endpoints": ["/tasks", "/health"] }
  ```
* **`GET /health`** — *Status Gateway.* Validates live connectivity metrics.
  ```json
  { "status": "ok" }
  ```

####  Task Management Array
* **`GET /tasks`** — Parses out the entire active array of data entries.
* **`GET /tasks/{id}`** — Pinpoints and renders a single target index record. Returns a strict `404 Not Found` if the index does not exist.
* **`POST /tasks`** — Inserts a payload string into storage. Processes ID generation sequentially. Returns `201 Created`. Drops a `400 Bad Request` if field metrics fail validation checks.
* **`PUT /tasks/{id}`** — Modifies structural properties (`title` or `done`) within an existing object.
* **`DELETE /tasks/{id}`** — Erases target object index from the workspace. Transmits a `204 No Content` code signature on successful execution profiles.

---

###  Data Architecture

```text
Task Instance
 ├── id        : Integer (Unique System Reference ID)
 ├── title     : String  (Task Title Data)
 └── done      : Boolean (Status Completion Flag)
```

```text
Workspace Topography
 .
 ├── main.py       # Main Application Layer
 └── README.md     # Documentation Engine
```

---

###  Constraints & Next Iterations

* **Volatile Architecture:** Runs strictly via a standard runtime dictionary loop. 
* **Roadmap Targets:** Transition tracking layers into localized SQLite configurations, migrate schema verification into static Pydantic classes, and wire user registration validation checks.
