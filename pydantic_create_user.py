from pydantic import BaseModel, Field, EmailStr
import uuid

class UserSchema(BaseModel):
    id : str
    email : EmailStr
    last_name : str = Field(alias = 'lastName')
    first_name : str = Field(alias = 'firstName')
    middle_name : str = Field(alias = 'middleName')

class CreateUserSchema(BaseModel):
    email: EmailStr
    password :str
    first_name : str = Field(alias = 'firstName')
    last_name : str = Field(alias = 'lastName')
    middle_name : str = Field(alias = 'middleName')

class CreateUserResponseSchema(BaseModel):
    user : UserSchema