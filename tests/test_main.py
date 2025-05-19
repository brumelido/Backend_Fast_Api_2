from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensagem" in response.json()

def test_hello_sem_nome():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá, mundo!"}

def test_hello_com_nome():
    response = client.get("/hello?name=Bruna")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá, Bruna!"}

def test_sum():
    response = client.get("/sum?a=3&b=4")
    assert response.status_code == 200
    assert response.json() == {"resultado": 7.0}
