from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int

    model_config = {
        "from_attributes": True
    }

class CreateProductRequest(BaseModel):
    name: str
    price: float
    stock: int