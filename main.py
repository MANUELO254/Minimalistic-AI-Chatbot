import os
import requests
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Fetch the API key from the .env file
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def chat_with_bot(prompt, model="mistralai/mixtral-8x7b-instruct"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    if not OPENROUTER_API_KEY:
        return "[ERROR] OpenRouter API key not found in environment."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    
    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[ERROR] {str(e)}"

if __name__ == "__main__":
    print("🤖 Chatbot using OpenRouter is running. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        reply = chat_with_bot(user_input)
        print(f"Assistant: {reply}\n")
