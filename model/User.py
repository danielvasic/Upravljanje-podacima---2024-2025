from pydantic import BaseModel, EmailStr, validator
from hashlib import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    first_name: str
    last_name: str

class LoginUser(User):
    email: EmailStr
    password: str

    @validator('password', pre=True, always=True)
    def password_hash (cls, password):
        return pwd_context.hash(password)