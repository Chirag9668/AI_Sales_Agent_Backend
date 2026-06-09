from fastapi import FastAPI
from api.chat import router as chat_router
from api.catalog import router as catalog_router
from api.health import router as health_router
from db.database import engine, base

base.metadata.create_all(bind=engine)
app = FastAPI(title = "Persist Sales Agent")

app.include_router(chat_router)
app.include_router(catalog_router)
app.include_router(health_router)

@app.get("/")
def get_root():
    return {"message": "The sales agent is up and running!"}
