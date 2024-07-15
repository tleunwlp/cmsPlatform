import openai
from flask import current_app

def generate_gpt_question(category):
    openai.api_key = current_app.config['OPENAI_API_KEY']
    client = openai.ChatCompletion()

    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates questions in Korean."},
        {"role": "user", "content": f"{category} 상황에서 자주 묻는 질문 하나만 텍스트로 생성해 주세요. 불필요한 텍스트는 포함하지 말아주세요."}
    ]

    response = client.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150
    )
    
    question = response.choices[0].message['content'].strip()
    return question