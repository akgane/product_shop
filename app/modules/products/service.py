from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.products.models import Product
from app.modules.products.schemas import CreateProductRequest


async def get_all_products(db: AsyncSession) -> list[Product]:
    result = await db.execute(select(Product))
    return list(result.scalars().all())


async def get_product_by_id(product_id: int, db: AsyncSession) -> Product:
    product = await db.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


async def create_product(data: CreateProductRequest, db: AsyncSession) -> Product:
    product = Product(name=data.name, price=data.price, stock=data.stock)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def update_product(product_id: int, data: CreateProductRequest, db: AsyncSession) -> Product:
    product = await get_product_by_id(product_id, db)
    product.name = data.name
    product.price = data.price
    product.stock = data.stock
    await db.commit()
    await db.refresh(product)
    return product


async def delete_product(product_id: int, db: AsyncSession) -> None:
    product = await get_product_by_id(product_id, db)
    await db.delete(product)
    await db.commit()
