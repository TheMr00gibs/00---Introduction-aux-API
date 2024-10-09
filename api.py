import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

'''
I - PATH PARAMETER
Request URL : GET http://www.localhost:8000/user/johndoe

Response header : 
    content-length: 23 
    content-type: application/json 
    date: Tue,10 Sep 2024 08:15:38 GMT 
    server: uvicorn 

Response body : { "user_name": "johndoe" }

Status code : 200
'''

@app.get("/user/{user_name}")
async def read_user(user_name : str) :
    return {"user_name" : user_name}


################################################################################################

'''
II - QUERY PARAMETER
Request URL : GET http://127.0.0.1:8000/items/?skip=0&limit=1

Response Body : [ { "item_name": "Foo" } ]

Response header : 
    content-length: 21 
    content-type: application/json 
    date: Tue,10 Sep 2024 08:40:54 GMT 
    server: uvicorn 

Status code : 200
'''

users = [{ "user_name" : "michaelScott", "Password" : "That's what she said"}, 
         {"user_name" : "JimHalper", "password" : "Dwight tried to kiss me"}, 
         {"user_name" : "dwightShrute", "password" : "I am faster than 80% of all snakes"}]

@app.get("/user/")
async def read_user(skip : int = 0, limit : int = 3) : 
    return users[skip: skip + limit]

################################################################################################

'''
III - REQUEST BODY PARAMETER
Request URL : http://localhost:8000/items/ 

Cuurl : 
    curl -X 'POST' \
        'http://localhost:8000/items/' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "name": "Hugo",
        "description": "Produit de luxe",
        "price": 3000000000,
        "tax": 0
    }'

Status code : 200

Response Body : 
    {
        "name": "Hugo",
        "description": "Produit de luxe",
        "price": 3000000000,
        "tax": 0
    }

Response Headers : 
    content-length: 78 
    content-type: application/json 
    date: Tue,10 Sep 2024 08:50:53 GMT 
    server: uvicorn 
'''

# To declare a request body, you use Pydantic models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item) : 
    return item

################################################################################################

if __name__ == "__main__" : 
    uvicorn.run(app, host="0.0.0.0", port=8000)