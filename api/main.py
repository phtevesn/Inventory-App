from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import health
from routers import users
from routers import inventory
from routers import skeletons
from routers import folder
from routers import skeleinstance
from routers import statuses
from routers import items 

app = FastAPI()
app.include_router(health.router)
app.include_router(users.router)
app.include_router(inventory.router)
app.include_router(skeletons.router)
app.include_router(folder.router)
app.include_router(skeleinstance.router)
app.include_router(statuses.router)
app.include_router(items.router)


app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000"],
  allow_credentials=True, 
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def root():
  return {"message": "This is your api"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
  
'''
 inv    | folders        | table | inventory   
 inv    | folderskeles   | table | inventory
 inv    | inventories    | table | inventory
 inv    | invskeles      | table | inventory
 inv    | invstatuses    | table | inventory
 inv    | items          | table | inventory
 inv    | skelechildren  | table | inventory
 inv    | skelefolders   | table | inventory
 inv    | skeleinstances | table | inventory
 inv    | skeleparents   | table | inventory
 inv    | skeletons      | table | inventory
 inv    | statuses       | table | inventory
 inv    | userinvs       | table | inventory
 inv    | userroles      | table | inventory
 inv    | users          | table | inventory
 inv    | userskelesfav  | table | inventory
 inv    | userstatusfav  | table | inventory

'''