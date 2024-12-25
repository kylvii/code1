from fastapi import FastAPI
from sqlalchemy.orm import Session
import uvicorn

from app.database import get_db, engine
from app.models import Base
from app.routes import user_router, product_router

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Ticaret API")

# Router'ları ekle
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/products", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Hoş geldiniz! E-Ticaret API'sine"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
