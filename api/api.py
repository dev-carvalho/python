# Autor: Marcos Antonio de Carvalho
# Descrição: Implementação de APIRest (CRUD) utilizando fastapi com modelagem de 
#            dados pydantic (models.py) e tratamento de exceção http.

# Referencias:
#   FastAPI Tutorial - Building RESTful APIs with Python
#   https://www.youtube.com/watch?v=GN6ICac3OXY

from typing  import List
from uuid    import UUID, uuid4

# pip3 install fastapi  
from fastapi import FastAPI, HTTPException

# models.py
from models  import Gender, Role, User, UserUpdateRequest  

app = FastAPI()

db: List[User] = [
    User(
        # uuid() é legal para criar um identicador aleatório 
        #id=uuid4(),
        id="8d7fdab4-e598-4863-a448-71188a952930",
        first_name="Jamile",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        #id=uuid4(), 
        id="07479d47-4df2-4dc6-accd-1d16ffde4844",
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),    
]

# Document - reservado para documentação da API exposta para o consumidor
@app.get("/api/v1/users/doc")
async def hello_world_root():
    return {"API Versão 1": "Documentação do consumidor"}

#
# Implementação do CRUD
#
# Create - adicionar 
# Read   - consultar
# Update - atualizar
# Delete - apagar

# Read - retorna p banco de dados
@app.get("/api/v1/users")
async def fetch_users():
    return db; 

# Create - adicionar um usuário
@app.post("/api/v1/users")
async def register_user(user: User): # usuário vem no 
    db.append(user)
    return{"id": user.id}

# Delete - apagar um usuário
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException( # tratar exceção http
        status_code=404,
        detail=f"usuário com id: {user_id} não existe!"
    ) 

# Update - atualizar um usuário
# desc.: solicita uma atualização para um determinado id
@app.put("/api/v1/users/{user_id}")
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
    raise HTTPException( # tratar exceção http
        status_code=404,
        detail=f"usuário com id: {user_id} não existe!"
    ) 
