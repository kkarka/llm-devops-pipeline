# LLM DevOps Pipeline Project

## 🚀 Overview
This project demonstrates an end-to-end deployment of a Large Language Model using FastAPI, Docker, and Kubernetes.

## Features (Phase 1)
- FastAPI-based LLM inference API
- GPT-2 model integration using HuggingFace Transformers
- CPU-based deployment (portable across environments)

## Tech Stack
- Python
- FastAPI
- Transformers
- PyTorch

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoint

POST /generate
```bash
{
  "prompt": "DevOps is"
}
```
