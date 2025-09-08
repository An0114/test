# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-24240352b44367466949c08c22bd176b9974e6", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你可以告诉我今天山西省晋中市榆次区的天气吗"},
    ],
    stream=False
)

print(response.choices[0].message.content)
