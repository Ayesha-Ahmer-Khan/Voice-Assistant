import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:4b"


def generate_response(user_text):
    payload = {
        "model": MODEL,
        "prompt": user_text,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()
    return data["response"]