# 🤖 OpenRouter Chatbot (Python Terminal App)

A minimal terminal-based AI chatbot powered by OpenRouter, using open-source models like Mistral, LLaMA 3, and GPT-3.5 — all without relying on OpenAI directly. API keys are securely stored in a `.env` file using `python-dotenv`.

---

## 📦 Features

- Talk to powerful models like Mixtral, Mistral 7B, LLaMA 3, GPT-3.5
- Better quotas than OpenAI (some providers are free)
- Fully terminal-based — no browser needed
- API key stored securely in `.env` file
- Easily customizable and extendable

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/MANUELO254/Minimalistic-AI-Chatbot.git
cd Minimalistic-AI-Chatbot

2. Install Requirements

pip install -r requirements.txt

If you don’t have a requirements.txt, just run:

pip install requests python-dotenv

3. Get Your OpenRouter API Key
Go to https://openrouter.ai

Sign in and visit https://openrouter.ai/keys

Copy your API key (starts with sk-or-...)

4. Create a .env File
In your project root, create a .env file:
OPENROUTER_API_KEY=sk-or-your-api-key-here
🔒 Never share or commit this file to GitHub!

5. Run the Chatbot
python main.py
You’ll see:

🤖 Chatbot using OpenRouter is running. Type 'exit' to quit.

You: What is the capital of Kenya?
Assistant: The capital of Kenya is Nairobi.

How It Works
Loads your API key securely from .env

Sends user input as a message to OpenRouter's /chat/completions API

Uses a selected model like mistralai/mixtral-8x7b-instruct

Prints the AI response in your terminal

🧪 Supported Models
You can change the model by editing this line in main.py:

model="mistralai/mixtral-8x7b-instruct"
Other great options:

"meta-llama/llama-3-8b-instruct"

"openchat/openchat-3.5-1210"

"openai/gpt-3.5-turbo"

👉 View full list: https://openrouter.ai/docs#models

🔒 Security
API keys are loaded via python-dotenv from .env

.env is excluded via .gitignore to avoid leaking credentials
