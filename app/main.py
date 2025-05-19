# app/main.py
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(
    title="Minha API Documentada com Swagger",
    description="Uma API simples com dois endpoints usando FastAPI e Swagger UI.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"mensagem": "API da Bruna no ar! Visite /docs para ver a documentação."}

@app.get("/hello")
def read_root(name: Optional[str] = Query(None, description="Nome da pessoa para cumprimentar")):
    if name:
        return {"message": f"Olá, {name}!"}
    return {"message": "Olá, mundo!"}

@app.get("/sum")
def sum_numbers(a: float = Query(..., description="Primeiro número"), b: float = Query(..., description="Segundo número")):
    return {"resultado": a + b}