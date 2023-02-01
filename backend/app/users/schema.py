from pydantic import (
    BaseModel,
    EmailStr,
    Field
)
from datetime import datetime

class UserRegister(BaseModel):
    username: str
    password: str
    email: EmailStr
    avatar: str = None
    is_super_user: bool = False
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

class UserLogin(BaseModel):
    username: str
    password: str