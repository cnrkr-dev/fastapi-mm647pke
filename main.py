from typing import Optional

from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Merhaba World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/merhaba/{sayi}")
def merhaba(sayi: int) -> List[str]: 
    return [f"merhaba {i}" for i in range(1, sayi + 1)]
