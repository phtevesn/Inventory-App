from fastapi import FastAPI
import uvicorn

from routers import health
from routers import users

app = FastAPI()
app.include_router(health.router)
app.include_router(users.router)

@app.get("/")
def root():
  return {"message": "This is your api"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)