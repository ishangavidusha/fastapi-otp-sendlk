from fastapi import FastAPI
from dotenv import load_dotenv
import sendlk
import os

# Load the .env file
load_dotenv(".env")

SENDLK_TOKEN = os.environ.get("SENDLK_TOKEN")
SECRET = os.environ.get("SECRET")

sendlk.initialize(SENDLK_TOKEN, SECRET)

# Imports routes
from src.route import router

# Create the app
app: FastAPI = FastAPI(
    title="FastAPI Mobile Verification",
    version="0.1.0",
)

# App Root
@app.get("/", name="root")
def root():
    return {"message": f"Welcome to Mobile Verification API {app.version}"}

app.include_router(router, prefix="/api")