from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import health
from routers import users
from routers import inventory

app = FastAPI()
app.include_router(health.router)
app.include_router(users.router)
app.include_router(inventory.router)

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