import json
import os
#from xinference.client import Client
from openai import OpenAI

#client = OpenAI(base_url="http://202.120.39.36:8800/v1", api_key="not used actually")

#response = client.chat.completions.create(
    #model="Qwen2-7B-Instruct",
    #max_tokens=4096,
    #messages=[
        #{"role": "system", "content": "You are a helpful assistant."},
        #{"role": "user", "content": "介绍一下自己?"}
    #]
#)
client = OpenAI(base_url="http://202.120.39.36:8800/v1", api_key="not used actually")
response = client = OpenAI(base_url="http://202.120.39.36:8800/v1", api_key="not used actually")
response = client.chat.completions.create(
    model="Qwen2-7B-Instruct",
    messages=[{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "介绍一下自己?"}],
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0
)

result = response.choices[0].message.content.strip()
print(response)