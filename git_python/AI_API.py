# Please install OpenAI SDK first: `pip3 install openai`
import os
import time

from openai import OpenAI

api_key = os.getenv("DASHSCOPE_DEEPSEEK_API_KEY")
url = "https://api.deepseek.com"

client = OpenAI(api_key=api_key, base_url=url)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是助手"},
        {"role": "user", "content": "世界第一高的山是什么"},
    ],
    # stream=False
)

text = response.choices[0].message.content
for ch in text:
    if ch == '\n':
        print()
    else:
        print(ch, end='', flush=True)
        time.sleep(0.1)

