from fastapi import FastAPI

from models.product import Product

from routers.product import router as product_router

app = FastAPI()


@app.get('/')

def message():
    return 'Hola Mundo'

app.include_router(product_router)
