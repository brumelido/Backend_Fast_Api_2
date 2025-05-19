from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth import authenticate_user, create_access_token, decode_token
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

# Middleware para proteger rotas
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload["sub"]
    except:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

@app.get("/hello")
def read_root(name: Optional[str] = None, user: str = Depends(get_current_user)):
    if name:
        return {"message": f"Olá, {name}!"}
    return {"message": f"Olá, {user}!"}

@app.get("/sum")
def sum_numbers(a: float, b: float, user: str = Depends(get_current_user)):
    return {"resultado": a + b}

@app.get("/")
def home():
    return {"mensagem": "API com autenticação JWT. Acesse http://127.0.0.1:8000/docs para testar."}