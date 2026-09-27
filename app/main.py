from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import Base, engine
from app.modules.products.router import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(products_router, prefix="/api/v1/products", tags=["products"])


@app.get("/")
async def root():
    return {"message": "Product shop API"}
