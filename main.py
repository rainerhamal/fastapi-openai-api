from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description

# ! Initialise FastAPI
app = FastAPI()

# ! Define your data model for product
class Order(BaseModel):
    product: str
    units: int

class Product(BaseModel):
    name: str
    notes: str

@app.get("/home")
async def ok_endpoint():
    return {"message": "ok"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.post("/orders")
async def place_order(product: str, units: int):
    return {"message": f"Order for {units} unit/s of {product} placed successfully"}


@app.post("/orders_pydantic")
async def place_orders(order: Order):
    return {"message": f"Order for {order.units} unit/s of {order.product} placed successfully."}

@app.post("/product_description")
async def generate_product_description(product: Product):
    description = generate_description(f"Product name: {product.name}, Notes: {product.notes}")
    return {"product_description": description}
    


