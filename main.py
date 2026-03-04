from typing import Optional

from fastapi import FastAPI, UploadFile, File
from typing import List
import csv 
import io
import requests
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


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

@app.get("/get-items/")
def get_items():
    url = f"{SUPABASE_URL}/rest/v1/fund_types"  # 'mytable' yerine tablo adını yaz
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
