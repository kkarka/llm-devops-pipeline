from transformers import pipeline

# Load model once 
generator = pipeline(
    "text-generation",
    model="gpt2",
    device=-1
)

def generate_text(prompt: str):
    result = generator(prompt, max_length=50)
    return result[0]["generated_text"]