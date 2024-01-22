from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from pydantic import BaseModel
from sql_app import models
from sql_app.database import  SessionLocal, engine
# please be aware on where are you running this so the imports will work - otherwise correct the folder imports
# from . import models
# from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#pydantinc models for querying ()
class InventoryBase(BaseModel):
    productid: str
    name: str
    quantity: int
    category: str
    subcategory: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


###### 1 -load db with tables for testing the API

from sqlalchemy import create_engine
import pandas as pd
engine = create_engine("sqlite:///./sql_app.db")
connection = engine.connect()
path_to_inventory_csv= '/Users/guilherme.petris/Desktop/Guilherme/dema_ai_test-1/data_csv/inventory.csv' ## please add your path here ie. '/Users/guilherme.petris/Desktop/Guilherme/dema_ai_test/data_csv/inventory.csv'
df = pd.read_csv(path_to_inventory_csv)
df.to_sql('inventory', engine, index=False, if_exists='replace')

result = connection.execute(f"SELECT * FROM inventory LIMIT 5")  # check if data has landed
connection.close()
####################



## API operations
# Requirements:
    # ● List Inventory: An endpoint/query to list inventory on the store. It returns a list of all
    # products, each item in the list containing information about the product and orders
    # placed on that product. This list endpoint should support pagination for querying data.
@app.get("/list_inventory_paginated/",)
def list_inventory(skip: int = 0,
                    limit: int = 100,
                    db: Session = Depends(get_db)):
    list_inv = db.query(models.Inventory).offset(skip).limit(limit).all()
    return list_inv

# ● Update Inventory: An endpoint/mutation to update the product information and
# available quantity for a particular product. It should return the updated product and its
# order data.
@app.put("/update_inventory_item/{productid}")
def update_single_product_inventory( p:InventoryBase,
    productid: str,
    db: Session = Depends(get_db)):
    
    product_search = db.query(models.Inventory).filter(models.Inventory.productid == productid).first()
    
    if product_search is None:
        HTTPException(status_code=404, detail=f"Item with {productid=} does not exist.")

    product_search.name = p.name
    product_search.quantity = p.quantity
    product_search.category = p.category
    product_search.subcategory = p.subcategory

    db.add(product_search)
    db.commit()

    return p

# Bonus points
# ● Filters support in List Inventory: The client should be able to query only products
# belonging to a particular category or subcategory. Another filter should be to only
# fetch items in stock.

@app.get("/list_inventory_filter_and_stock/",)
def list_inventory_filter(db: Session = Depends(get_db),
                    categoryfilter: str = None,
                    subcategoryfilter: str = None,
                    in_stock: bool = None):
        
    list_inv = db.query(models.Inventory)\
        .filter(
        or_(models.Inventory.category == f'{categoryfilter}',
            models.Inventory.subcategory == f'{subcategoryfilter}'))
    if in_stock:
        list_inv = list_inv.filter(models.Inventory.quantity >= 1)
    
    return list_inv.all()

# ● Sorting support for List Inventory: The client should be able to specify the sorting
# order of returned list of products. It can be sorted based on product quantity in stock
# or number of orders placed for a product.

# @app.get("/list_inventory_sorted/",)
# def list_inventory_filter(db: Session = Depends(get_db),
#                     productquantity: str = None,
#                     subcategoryfilter: str = None,
#                     in_stock: bool = None):
        
#     list_inv = db.query(models.Inventory)\
#         .filter(
#         or_(models.Inventory.category == f'{categoryfilter}',
#             models.Inventory.subcategory == f'{subcategoryfilter}'))
#     if in_stock:
#         list_inv = list_inv.filter(models.Inventory.quantity >= 1)
    
#     return list_inv.all()


# ● Bulk update support for Update Inventory: The client can specify multiple products to
# be updated at once.



