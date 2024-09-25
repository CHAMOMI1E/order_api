from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.routers import product, order

app = FastAPI()

app.include_router(product.product_router, prefix="/products", tags=["products"])
app.include_router(order.order_router, prefix="/order", tags=["order"])


@app.get("/")
async def root():
    return {"message": "Start complite"}


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Страница не найдена. Проверьте URL и повторите попытку."
            },
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

