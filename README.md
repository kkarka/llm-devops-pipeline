# LLM DevOps Pipeline Project

## 🚀 Overview
This project demonstrates an end-to-end deployment of a Large Language Model using FastAPI, Docker, and Kubernetes.

## Architecture

Client → FastAPI → LLM (GPT-2) → Response

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


## Challenges Faced

- CUDA compatibility issue with PyTorch
- Resolved by using CPU-based deployment
- Ensured portability for Docker & Kubernetes


## Future Enhancements

- Dockerization
- Kubernetes deployment
- CI/CD pipeline (Jenkins)
- Monitoring (Prometheus + Grafana)
