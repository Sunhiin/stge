import openai
import requests
                 



def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Tutor. Who answers brief questions about AI."},
        {"role": "user", "content": "I want to learn AI"},
        {"role": "assistant", "content": "Thats awesome, what do you want to know about AI"}
    ]
    return messages


def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
