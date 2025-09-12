# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-24b44367466949c08c22bd176b9974e6", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是天气预报助手"},
        {"role": "user", "content": "榆次区的天气怎么样"},
    ],
    stream=False
)

print(response.choices[0].message.content)
