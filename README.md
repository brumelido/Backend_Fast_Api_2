# 🔐 API com Autenticação JWT – FastAPI

Este projeto foi desenvolvido como parte da disciplina **Programação de Aplicativos Mobile**, ministrada pelo professor **Ricardo Casseb**, no curso de Ciência da Computação do CESUPA.

## 🎯 Objetivo

**Atividade 3 – Autenticação com JWT**

O objetivo foi adicionar uma camada de autenticação à API REST criada anteriormente, utilizando o padrão JWT (JSON Web Token). Apenas usuários autenticados podem acessar rotas protegidas da aplicação.

## ✅ Funcionalidades

- `POST /login`: autentica o usuário e retorna um token JWT
- `GET /hello`: retorna uma saudação personalizada (rota protegida)
- `GET /sum`: realiza a soma de dois números (rota protegida)

## 🔐 Como usar a autenticação

1. Acesse a documentação da API em [`/docs`](http://127.0.0.1:8000/docs)
2. Vá até o endpoint `POST /login`
3. Clique em **"Try it out"**
4. Informe as credenciais:
   - `grant_type`: `password`
   - `username`: `bruna@email.com`
   - `password`: `123456`
5. Clique em **"Execute"**
6. Copie o valor do campo `access_token`
7. Clique no botão **"Authorize"** no topo da página
8. Cole o token no formato:
   ```
   Bearer SEU_TOKEN
   ```
9. Agora você pode acessar normalmente as rotas `/hello` e `/sum`

## 📦 Tecnologias utilizadas

- FastAPI
- PyJWT
- passlib (bcrypt)
- python-multipart
- Swagger UI para testes interativos

## 👩‍💻 Autoria

**Bruna Melido**  
📧 brunamelido@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/brunamelido/)
