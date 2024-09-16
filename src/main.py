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

our_first_message = client.messages.create(
  model='claude-3-haiku-20240307',
  max_tokens=1000,
  messages=[{
    'role':'user',
    'content':'Hi, please write a haiku for me.'
  }]
)

print(our_first_message.content[0].text)