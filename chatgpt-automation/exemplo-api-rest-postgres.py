# Ptrograma gerado em resposta a solicitação:
#
# py gpt.py "api grud padrão rest utilizando fastapi e conexao com postgres para guardar uuid, nome do usuario, email, senha" exemplo-api-rest-postgres.py
#

import uuid

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import psycopg2

app = FastAPI()

# Create table
connec = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="postgres")
cursor = connec.cursor()
cursor.execute(
    """
    CREATE TABLE users (
        id  UUID PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
    """
)
connec.commit()
connec.close()


# Data Model
class UserIn(BaseModel):
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    id: uuid.UUID
    username: str
    email: str
    password: str


# CRUD (Create, Read, Update and Delete)
@app.post("/users/create")
def create_user(user: UserIn):
    id = uuid.uuid1()

    connec = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="postgres")
    cursor = connec.cursor()
    cursor.execute(
        f"INSERT INTO users (id, username, email, password) VALUES ('{id}', '{user.username}', '{user.email}', '{user.password}');"
    )
    connec.commit()
    connec.close()

    return UserOut(id=id, username=user.username, email=user.email, password=user.password)


@app.get("/users/read")
def read_users():
    connec = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="postgres")
    cursor = connec.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    users = []
    for record in records:
        user = UserOut(id=record[0], username=record[1], email=record[2], password=record[3])
        users.append(user)

    connec.commit()
    connec.close()

    return users
    

@app.put("/users/update/{id}")
def update_user(id: uuid.UUID, user: UserIn):
    connec = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="postgres")
    cursor = connec.cursor()
    cursor.execute(
        f"UPDATE users SET username='{user.username}', email='{user.email}', password='{user.password}' WHERE id='{id}';"
    )
    connec.commit()
    connec.close()

    return UserOut(id=id, username=user.username, email=user.email, password=user.password)


@app.delete("/users/delete/{id}")
def delete_user(id: uuid.UUID):
    connec = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="postgres")
    cursor = connec.cursor()
    cursor.execute(f"DELETE FROM users WHERE id='{id}';")
    connec.commit()
    connec.close()

    return {"message": "User deleted"}