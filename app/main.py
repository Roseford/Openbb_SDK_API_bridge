from fastapi import FastAPI
from app.routers import crypto
from app.routers import stocks
from app.routers import news


app = FastAPI()

app.include_router(news.router)
app.include_router(crypto.router)
app.include_router(stocks.router)

