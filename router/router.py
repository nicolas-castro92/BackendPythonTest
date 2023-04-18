from fastapi import APIRouter
from schema.user_schema import UserSchema
from config.db import conn
from model.users import users

user = APIRouter()

@user.get("/")
def root():
    return {"message:":"I am FastAPI router"}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    nuevo = data_user.dict()
    conn.execute(users.insert().values(nuevo))
    conn.commit()
    print(data_user)
    print(nuevo)
    return "Sucess"

@user.put("/api/user")
def update_user():
    pass