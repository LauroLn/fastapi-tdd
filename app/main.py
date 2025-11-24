from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de dados simples
ITEMS = {
    1: {"id": 1, "nome": "Item 1"}
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in ITEMS:
        return ITEMS[item_id]
    raise HTTPException(status_code=404, detail="Item não existe")
