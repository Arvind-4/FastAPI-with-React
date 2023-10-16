from fastapi import (
    APIRouter,
    Request,
    Response,
)

from app.users.auth import (
    create_access_token, 
    verify_token,
)
from app.users.hashes import Hash
from app.users.schema import (
    UserRegister,
    UserLogin,
)
from app.db.mongoclient import get_collection

router = APIRouter(prefix="/api")

@router.post('/users/register')
def create_user(user:UserRegister, request: Request, response: Response):
    hashed_pass = Hash.bcrypt(user.password)
    collection = get_collection()
    user_data = {
        "username": user.username,
        "email": user.email,
        "password": hashed_pass
    }
    existing_username = collection.find_one({"username": user.username})
    existing_email = collection.find_one({"email": user.email})
    if existing_email is not None:
        response.status_code = 400
        return {"message": "Email already exists"}
    if existing_username is not None:
        response.status_code = 400
        return {"message": "Username already exists"}
    else:
        new_user = collection.insert_one(user_data)
        print("User created", new_user)
        return {"message": "User created", "user": user_data}
    
@router.post('/users/login')
def login(user: UserLogin, request: Request, response: Response):
    collection = get_collection()
    find_user = collection.find_one({"username":user.username})
    if not find_user:
        response.status_code = 400
        return {"message": "User does not exist"}
    if Hash.verify(normal=str(user.password), hashed=str(find_user.get("password"))):
        access_token = create_access_token(data={"username": find_user.get("username")})
        awe = verify_token(token=access_token)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        response.status_code = 400
        return {"message": "Invalid credentials"}
    

@router.get('/users/all')
def get_all_users(request: Request, response: Response):
    collection = get_collection()
    users = collection.find({}, {"_id": 0})
    return {"users": tuple(users)}