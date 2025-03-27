from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: str
    street: str
    zip: Optional[int] = None

class Person(BaseModel):
    name: str
    address: Address


if __name__ == "__main__":
    a = Address(city="CB", street="Krajinska", zip="37001")
    p = Person(name="Bob", address=a)

    json_data = p.model_dump_json()

    # json_data poslano pres internet pres REST API

    p2 = Person.model_validate_json(json_data)
    
    print(p is p2)