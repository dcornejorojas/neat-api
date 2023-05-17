from pydantic import BaseModel


class Pokemon(BaseModel):
    name: str
    lastname: str
    address: str
    dni: str
    description: str
    extra: str
    is_sick: bool
    was_adopted: bool