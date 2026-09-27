from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.products import service
from app.modules.products.schemas import CreateProductRequest, ProductResponse

router = APIRouter()


@router.get("", response_model=list[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    return await service.get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_product_by_id(product_id, db)


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(data: CreateProductRequest, db: AsyncSession = Depends(get_db)):
    return await service.create_product(data, db)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, data: CreateProductRequest, db: AsyncSession = Depends(get_db)):
    return await service.update_product(product_id, data, db)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    await service.delete_product(product_id, db)
