from typing import Optional

from fastapi import FastAPI, UploadFile, File
from typing import List
import csv 
import io

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

@app.post("/upload-csv/") 
async def upload_csv(file: UploadFile = File(...)):
    # Dosya içeriğini oku
    content = await file.read()
    # Bytes -> string
    decoded = content.decode("utf-8")
    # String -> satır listesi 
    reader = csv.reader(io.StringIO(decoded)) 

    # CSV içeriğini listeye dönüştür 
    rows = [row for row in reader]
    
    return {"filename": file.filename, "rows": rows}
