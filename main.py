from pymongo import MongoClient
from fastapi import FastAPI
from model.User import User, LoginUser
from typing import List

client = MongoClient('mongodb://localhost:27017/')

db = client['db2025']
users_collection = db['users']

app = FastAPI()

@app.post("/user", response_model=User)
def create_user(user: User):
    users_collection.insert_one(user.dict())
    return user

@app.get("/users", response_model=List[User])
def get_users():
    return users_collection.find()