import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.main.routes.v1 import (
    people_routes
)

load_dotenv()

# TODO: add configure to Logging Level

# Core Application Instance
app = FastAPI(
    title="Visie CRUD",
    version="v0.0.1",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"]
)

# Add Routers
app.include_router(people_routes.router)
