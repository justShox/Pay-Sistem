from fastapi import FastAPI
from transaction.currency_api import currency_router

app = FastAPI(docs_url='/')

app.include_router(currency_router)