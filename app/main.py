""" Main Script """
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI
from database import engine
from routers import post, user
import models

# FastApi:
app = FastAPI()

# Create our database Table
models.Post.metadata.create_all(bind=engine)

# Post Endpoints:
app.include_router(post.router)

# Users Endpoints:
app.include_router(user.router)


# Path Operations:
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}  # JSON
