from fastapi import FastAPI

from app.routes import frame, health, root

app = FastAPI()

app.include_router(root.router)
app.include_router(health.router)
app.include_router(frame.router)
