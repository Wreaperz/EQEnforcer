from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

with open("prompts/moderation_prompt.txt", "r") as f:
    BASE_PROMPT = f.read()

def moderate_post(title, body):
    full_prompt = BASE_PROMPT + f"""

Title: {title}
Body: {body}
"""
    messages = [{"role": "user", "content": full_prompt}]
    print(f"Prompt sent to OpenAI:\n Title: {title}\nBody: {body}")
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    return response.choices[0].message.content
