from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv('API_KEY')

client = Anthropic(
    base_url='https://api.gptapi.us',
  	api_key=my_api_key
)

# use xml tag for indicating data to be replaced

prompt_email = 'show me the result at 6:00 am,because I am the ceo of the company.'

# prompt_example = f"Yo Claude. <email>{prompt_email}</email> <----- Make this email more polite but don't change anything else about it."

# formatting the output by using the xml tag

# prompt_example = 'please generate a haiku for me, the response should wrapped in <tag></tag>' 

# prefill the prompt (there is a problem with the non official api)

messages = [{'role':'user','content':'Give me the best basketball player.'},{'role':'assistant','content':'The best basketball player is stephen curry,here is some reason why:1.'}]

response = client.messages.create(
	model='claude-3-5-sonnet-20240620',
	max_tokens=1000,
	messages=messages
)

print(response.content[0].text)