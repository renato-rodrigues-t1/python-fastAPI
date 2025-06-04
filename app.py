from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Hello Reeeliance"}

@app.get("/users")
def get_users():
    return [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}, {"name": "David", "age": 28}, {"name": "Eve", "age": 22}, {"name": "Frank", "age": 40}]

@app.get("/greet/{username}")
def greet_user(username: str):
    return {"message": f"Hello {username}"}

@app.post("/user")
def create_user(user: User):
    return {"message": f"Created User {user.name} with {user.age} years old"}
