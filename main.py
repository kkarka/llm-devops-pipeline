from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load model once (IMPORTANT)
generator = pipeline("text-generation", model="gpt2", device=-1)

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
    result = generator(req.prompt, max_length=50)
    return {"output": result[0]["generated_text"]}