# dema_ai | Code Test

Hello and welcome to this repo - "clap, clap, clap"

# What was done:
- List inventory endpoint, including pagination
- Update inventory endpoint  - update a product's name, quantity, category and/or subcategory
- List inventory endpoint for filtering by name, category and subcategory
## What's missing:
- Bulk update support for Update Inventory
- Sorting support for List Inventory

## Instructions & Steps
 1. The solutions was made using FASTAPI - please verify if you have the requirements in requirementx.txt,
otherwise please install those

 2. Access ***main.py*** and please adjust the path of  the variable ***path_to_inventory_csv*** where the ***inventory.csv*** is actually located
***This is necessary to make it run smoothly***

 3. We gonna create a internal server for testing our API requests:

Please in a new terminal type the command and make sure you are acessing the root to be able to run uvicor from this setup:
```
uvicorn sql_app.main:app --reload 
```
The data of inventory should be already uploaded and a sql_app.db will be created in the root!

 4. Open your browser at: 
```
http://127.0.0.1:8000/docs
```
and verify methods

PS: The update method will require your input in the request_body in the UI for testing

## If i had more time

- Solve the rest of the bonus exercises
- Endpoint to sustain all the functions in just one: pagination,filtering,sorting
- Endpoint to check orders X inventory and maybe build an expectation inventory count after count, maybe grabbbing average number of orders for some inference...
- Test with moderm framework that can be dynamic and grow by the specifications of the request (GraphQL)
- Containerized for testing

