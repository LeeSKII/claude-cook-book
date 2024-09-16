from turtle import mode
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv('API_KEY')

client = Anthropic(
    base_url='https://api.gptapi.us',
  	api_key=my_api_key
)

conversation_history = []

while True:
    user_input = input("You: ")
    if user_input == 'quit':
        break
    conversation_history.append({'user':user_input})
    response = client.messages.create(
        model='claude-3-5-sonnet-20240620',
        messages=conversation_history,
        max_tokens=500,
    )
    response_text = response.content[0].text
    print("Assistant:", response_text)
    conversation_history.append({'assistant':response_text})