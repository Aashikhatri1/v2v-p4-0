import openai
from dotenv import load_dotenv
import os
import json
import re

# Load environment variables from .env file
load_dotenv()

# Access environment variables
PPLX_API_KEY = os.environ.get("PPLX_API_KEY")
os.environ["PPLX_API_KEY"] = PPLX_API_KEY

model_name="llama-2-70b-chat"

# query = input('user:')

def query_step_1(query):
    messages = [
        {
            "role": "system",
            "content": (
            '''You are a Hotel receptionist who provides responses to customer queries
            Respond with a Question category as json format {"category":"<>"}. Values can be Billing, product Info, FAQs
            FAQ questions include "What is your name?", "Is this the Grand Holiday Hotel?", "Do you have room service?", "Do you have Wi-Fi?", "What's the checkout time?"
            Always respond with following json format {"Category": "<category>"}'''
            ),
        }
    ]

    messages.append({"role": "user", "content": query})

    # Chat completion with streaming
    response_stream = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
        api_base="https://api.perplexity.ai",
        api_key=PPLX_API_KEY,
        stream=True,
    )

    final_answer = ""
    for response in response_stream:
        if 'choices' in response:
            content = response['choices'][0]['message']['content'].strip()
            if content:  # This condition might need to be adjusted
                final_answer = content

    # After the loop, print the final answer
    print('final answer:', final_answer)


    # Regular expression pattern to find JSON-like structure
    # This is a simple pattern and might need adjustments based on actual content
    pattern = r'\{.*?\}'

    # Search for JSON-like strings
    matches = re.findall(pattern, final_answer)
    print(matches)
    

# query_step_1(query)