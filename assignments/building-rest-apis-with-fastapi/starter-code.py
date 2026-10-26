from fastapi import FastAPI

app = FastAPI()

# Sample in-memory data store
items = [
    {"id": 1, "name": "Read API docs", "done": False},
    {"id": 2, "name": "Build a FastAPI app", "done": True},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add GET /items
# TODO: Add POST /items
# TODO: Add GET /items/{item_id}
# TODO: Add validation and extra API features
