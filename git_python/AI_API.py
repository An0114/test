# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

api_key = os.getenv("DASHSCOPE_DEEPSEEK_API_KEY")
url = "https://api.deepseek.com"
client = OpenAI(api_key=api_key, base_url=url)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是天气预报助手"},
        {"role": "user", "content": "榆次区的天气怎么样"},
    ],
    stream=False
)

print(response.choices[0].message.content)
