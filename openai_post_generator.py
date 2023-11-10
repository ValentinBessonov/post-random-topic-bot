import json
from openai import OpenAI

with open('config.json', 'r') as f:
    config = json.load(f)

API_KEY = config.get('openai_api_key')
SYSTEM_INSTRUCTIONS = config.get('openai_system_prompt')

def generate_post(topic):
    client = OpenAI(
        api_key=API_KEY,
    )
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": SYSTEM_INSTRUCTIONS
            },
            {
            "role": "user",
            "content": topic
            }
        ],
        temperature=1,
        max_tokens=2002,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return completion.choices[0].message.content

if __name__ == '__main__':
    topic = 'Greetings'
    post = generate_post(topic)
    print(post)