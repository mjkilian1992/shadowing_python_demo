from pydantic import BaseModel, EmailStr


class CustomerEntity(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str


class CustomerCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class CustomerUnsubscribe(BaseModel):
    email: EmailStr
