# Autor: Marcos Antonio de Carvalho
# Descrição: Implementação de APIRest (CRUD) utilizando fastapi com modelagem de
#            dados pydantic (models.py) e tratamento de exceção http.

# Referencias:
#   FastAPI Tutorial - Building RESTful APIs with Python
#   https://www.youtube.com/watch?v=GN6ICac3OXY

from fastapi import Response
from fastapi import Cookie
from typing import Optional, List
from uuid import UUID, uuid4

# Servidor ASGI (WebServer)
import uvicorn

# pip3 install fastapi
from fastapi import FastAPI, HTTPException

# models.py
from models import Gender, Role, User, UserUpdateRequest

#app = FastAPI()

# Auto-documentação da API está exposta para o consumidor em  "/docs"
#  Referências na construção
#  https://fastapi.tiangolo.com/tutorial/metadata/

# Dica - O campo description pode ser escrito com Markdown que será renderizado na saída.
description = """
### API REST escrita em Pythom utilizando a FastAPI vai ajudar a fazer coisas incriveis. 🚀
---
#### Users: Operations with users. The **login** logic is also here.

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="USER",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)



db: List[User] = [
    User(
        # uuid() é legal para criar um identicador aleatório
        # id=uuid4(),
        id="8d7fdab4-e598-4863-a448-71188a952930",
        first_name="Jamile",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        # id=uuid4(),
        id="07479d47-4df2-4dc6-accd-1d16ffde4844",
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
]


#
# Implementação do CRUD
#
# Create - adicionar
# Read   - consultar
# Update - atualizar
# Delete - apagar

# Read - retorna p banco de dados


@app.get("/users")
async def fetch_users():
    return db

# Create - adicionar um usuário


@app.post("/users")
async def register_user(user: User):  # usuário vem no
    db.append(user)
    return {"id": user.id}

# Delete - apagar um usuário


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(  # tratar exceção http
        status_code=404,
        detail=f"usuário com id: {user_id} não existe!"
    )

# Update - atualizar um usuário
# desc.: solicita uma atualização para um determinado id


@app.put("/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(  # tratar exceção http
        status_code=404,
        detail=f"usuário com id: {user_id} não existe!"
    )


#
# Manipulação de Cookie
# https://docs.roy4801.tw/Programming%20Language/python/libs/fastapi/
#

# getCookie - Recupera um Cookie existente


@app.get('/getCookie')
def get_cookie(test: Optional[str] = Cookie(...)):
    return test


# setCookie - Guarda um valor em um Cookie


@app.get('/setCookie')
def set_cookie(response: Response):
    response.set_cookie(key='test', value='fuck you')
    return {'message': 'success'}


# Ativa o serviço em produção
# Isso aqui eu aprendi perguntando para o chatGPT
#if __name__ == '__main__':
#    uvicorn.run(app, host="0.0.0.0", port=8000)


# Ativa o Serviço em Desenvolvimento
# “--reload”  é responsável toda vez que atualizar o projeto
# uvicorn api:app --reload
