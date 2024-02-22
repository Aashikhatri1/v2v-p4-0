
import faiss_code

# The pattern to search for
def response_type(query, category):
    FAQ = '{"Category": "FAQs"}'

    # Check if the pattern is in the string
    if FAQ in category:
        # print("yes")     ## run faiss code
        faiss_code.get_faiss_response(query)
    else:
        print("no")   # run fetch data.py


#### 5 A
    
# import json

# # Path to your JSON file
# filename = 'data.json'

# # Load JSON data from the file
# with open(filename, 'r') as file:
#     data = json.load(file)

# criteria = {
#     "Category": "Billing",
#     "Sub Category": "Payment issue",
#     "Sub Sub Category": "- Solutions for payment problems",
# }

# # Function to find the matching information
# def find_information(data, criteria):
#     for item in data:
#         if all(item[key] == value for key, value in criteria.items()):
#             return item.get("Information")  # Return the matching information
#     return "Information not found"  # Return a default message if no match is found

# # Use the function and store the result in the variable 'info'
# info = find_information(data, criteria)

# print(info)


# ## 5 B


# import openai
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Access environment variables
# PPLX_API_KEY = os.environ.get("PPLX_API_KEY")
# os.environ["PPLX_API_KEY"] = PPLX_API_KEY

# model_name="llama-2-70b-chat"

# def step5B(chat_history, query, info):
#     messages = [
#         {
#             "role": "system",
#             "content": (
#             '''You are a Hotel receptionist who provides responses to customer queries
#             Respond to the user query according to the chat history and the relevant information provided.
#             ''' + f'Information: {info}' + f'chat_history: {chat_history}'
#             ),
#         }
#     ]

#     messages.append({"role": "user", "content": f'user query: {query}'})


#     # Chat completion with streaming
#     response_stream = openai.ChatCompletion.create(
#         model=model_name,
#         messages=messages,
#         api_base="https://api.perplexity.ai",
#         api_key=PPLX_API_KEY,
#         stream=True,
#     )

#     final_answer = ""
#     for response in response_stream:
#         if 'choices' in response:
#             content = response['choices'][0]['message']['content'].strip()
#             if content:  # This condition might need to be adjusted
#                 final_answer = content

#     # After the loop, print the final answer
#     print('final answer:', final_answer)
#     return final_answer


    
    
# step5B(chat_history, query, info)