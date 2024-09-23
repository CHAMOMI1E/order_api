from fastapi import APIRouter


product_router = APIRouter()


@product_router.get("/")
async def get_products():
    """
    db.add_products() -> products
    """
    return {"products": "list of products"}
