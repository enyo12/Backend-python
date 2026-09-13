"""
Beginner Starter Backend API with FastAPI

A simple, production-ready Python backend you can deploy on Render.
Includes:
- Health check endpoint
- Root welcome endpoint
- Simple in-memory Items CRUD (for learning)
- Automatic interactive docs at /docs

Run locally: uvicorn main:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Beginner Starter Backend",
    description="A simple FastAPI backend ready to deploy on Render.com",
    version="1.0.0",
)

# ---------- Models ----------

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Learn FastAPI")
    description: Optional[str] = Field(None, max_length=500, example="Build a starter backend")


class Item(ItemCreate):
    id: int
    created_at: datetime


# ---------- In-memory "database" (resets on restart) ----------

items_db: List[Item] = []
next_id = 1


# ---------- Endpoints ----------

@app.get("/")
def root():
    """Welcome endpoint – returns basic info about the API."""
    return {
        "message": "Hello from your beginner Python backend! 🚀",
        "docs": "/docs",
        "health": "/health",
        "items": "/items",
    }


@app.get("/health")
def health_check():
    """Simple health check used by monitoring / load balancers."""
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


@app.get("/items", response_model=List[Item])
def list_items():
    """Return all items currently stored in memory."""
    return items_db


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    """Create a new item and store it in memory."""
    global next_id
    new_item = Item(
        id=next_id,
        name=item.name,
        description=item.description,
        created_at=datetime.utcnow(),
    )
    items_db.append(new_item)
    next_id += 1
    return new_item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Retrieve a single item by its ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item by its ID."""
    global items_db
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")


# Optional: run with `python main.py` for quick local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
