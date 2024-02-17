from typing import List
from fastapi import FastAPI
from models import User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid.uuid4(),
        first_name="Samuel",
        last_name="Adeola",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
       User(
        id=uuid4(), 
        first_name="Sola",
        last_name="Somuyiwa",
        gender=Gender.female,
        roles=[Role.student]
    ),
]
@app.get("/")
async def root():
    return {"Hello":"world My name is samuel Adeola, i am currently building my api"}
            
@app.get("/api/v1/users")
async def fetch_users():
    return db;