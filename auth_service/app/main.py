from fastapi import FastAPI, Depends
from app.routers.users_router import router as users_router

app = FastAPI()

app.include_router(users_router)

@app.get("/")
def home_page():
    print('123')
    return {"message": "bro service"}