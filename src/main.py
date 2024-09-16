from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv('API_KEY')

client = Anthropic(
    base_url='https://api.gptapi.us',
  	api_key=my_api_key
)

def translate(text:str,target_language:str='English'):
    prompt = f"Translate the text from {text} to {target_language}. Respond with a single world or phrase."
    response = client.messages.create(
		model='claude-3-5-sonnet-20240620',
		max_tokens=50,
		messages=[{
			'role':'user',
			'content':prompt
		}]
	)
    return response.content[0].text

# response = client.messages.create(
# 	model='claude-3-5-sonnet-20240620',
# 	max_tokens=1000,
# 	messages=[{
# 		'role':'user',
# 		'content':'What flavors are used in Dr. Pepper?'
# 	}]
# )

# putting words in Claude's mouth 

# response = client.messages.create(
# 	model='claude-3-haiku-20240307',
# 	max_tokens=100,
# 	messages=[{
# 		'role':'user',
# 		'content':'Generate a beautiful haiku'
# 	},{'role':'assistant','content':'swimming in the ocean'}]
# )

# few-shot prompting

response = client.messages.create(
    model='claude-3-5-sonnet-20240620',
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
    ]
)
print(response.content[0].text)


# print(translate('helo', 'French'))