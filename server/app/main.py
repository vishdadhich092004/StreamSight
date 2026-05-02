from fastapi import FastAPI

from app.routes import health, root

app = FastAPI()

app.include_router(root.router)
app.include_router(health.router)
