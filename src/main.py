from anthropic import Anthropic
from dotenv import load_dotenv
import os
import time
import base64
from pathlib import Path

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

# print(translate('helo', 'French'))

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

# response = client.messages.create(
#     model='claude-3-5-sonnet-20240620',
#     max_tokens=500,
#     messages=[
#         {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
#         {"role": "assistant", "content": "NEGATIVE"},
#         {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
#         {"role": "assistant", "content": "POSITIVE"},
#         {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
#         {"role": "assistant", "content": "NEGATIVE"},
#         {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
#     ]
# )
# print(response.content[0].text)

# stop_sequence

# response = client.messages.create(
# 	model='claude-3-5-sonnet-20240620',
# 	max_tokens=10,
# 	messages=[{
# 		'role':'user',
# 		'content':'Generate a json object representing a person with the following properties:name,age.'
# 	}],
# 	stop_sequences=['}']
# )
# print(response.content[0].text)
# print(response.stop_reason)

# system prompts

# response = client.messages.create(
# 	model='claude-3-5-sonnet-20240620',
# 	max_tokens=1000,
#     system='you are a language tutorial bot, respond every question with French.',
# 	messages=[{
# 		'role':'user',
# 		'content':'give me a definition of cold with a French translation.'
# 	}],
# 	stop_sequences=['}']
# )
# print(response.content[0].text)
# print(response.stop_reason)

# stream

# start_time = time.time()

# stream = client.messages.create(
#     model='claude-3-5-sonnet-20240620',
#     max_tokens=1000,
#     stream=True,
#     messages=[{
#         'role':'user',
#         'content':'What is the meaning of life?'
#     }]
# )

# first_receive_time = time.time()

# for event in stream:
#     if event.type == 'content_block_delta':
#         print(event.delta.text,flush=True,end='')

# end_time = time.time()

# print(f"Time taken to receive first response: {first_receive_time-start_time} seconds")
# print(f"Time taken to receive all responses: {end_time-first_receive_time} seconds")

# vision capabilities

# with open('d:/projects/claude/images/images.jpg','rb') as image_file:
#     binary_data = image_file.read()
#     base64_data = base64.b64encode(binary_data)
#     base64_string = base64_data.decode('utf-8')
    
base64_string = base64.b64encode(Path('./images/images.jpg').absolute().read_bytes()).decode('utf-8')

base64_animal1 = base64.b64encode(Path('./images/a1.png').absolute().read_bytes()).decode('utf-8')
base64_animal2 = base64.b64encode(Path('./images/a2.png').absolute().read_bytes()).decode('utf-8')
base64_animal3 = base64.b64encode(Path('./images/a3.png').absolute().read_bytes()).decode('utf-8')

response = client.messages.create(
    model='claude-3-5-sonnet-20240620',
    max_tokens=1000,
    messages=[
        {
            'role':'user',
            'content':[
                # {
                #     'type':'image',
                #     'source':{
                #     'type':'base64',
                #     'data':base64_string,
                #     'media_type':'image/jpeg'
                #     }
                # },
                {
                    'type':'image',
                    'source':{
                    'type':'base64',
                    'data':base64_animal1,
                    'media_type':'image/png'
                    }
                },
                {
                    'type':'image',
                    'source':{
                    'type':'base64',
                    'data':base64_animal2,
                    'media_type':'image/png'
                    }
                },
                {
                    'type':'image',
                    'source':{
                    'type':'base64',
                    'data':base64_animal3,
                    'media_type':'image/png'
                    }
                },
                {
                    'type':'text',
                    'text':'How are these images different?'
                }
                # {
                #     'type':'text',
                #     'text':'How many people in this picture? respond with a number.'
                # }
             ]
        }
    ]
)

print(response.content[0].text)