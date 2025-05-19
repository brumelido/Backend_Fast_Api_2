import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

# Simulação de usuário no bd
fake_user = {
    "email": "bruna@email.com",
    "password": "$2b$12$LOjmVRY0W2AA5zeeakmN4e.RRabrCKgcsh8blRi7DzSLpS6qyWDFu"  # senha: 123456
}


SECRET_KEY = "minha-chave-secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str):
    if email != fake_user["email"]:
        return False
    if not verify_password(password, fake_user["password"]):
        return False
    return True

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])