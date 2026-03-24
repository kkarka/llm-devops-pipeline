from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Define request schema
class Request(BaseModel):
    prompt: str

# Health check endpoint
@app.get("/")
def health():
    return {"status": "running"}

# Main inference endpoint
@app.post("/generate")
def generate(req: Request):
    return {"output": generate_text(req.prompt)}