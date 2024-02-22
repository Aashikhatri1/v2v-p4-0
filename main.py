
import csv2json
import step2
import sys
import step5

sys.path.append("./components")

import speech_to_text1


# csv2json.convert_csv_to_json('data.csv')  #converting csv to json

# query = speech_to_text1.transcribe_stream()
# print(query)
# category = step2.query_step_1(query)
# print(category)

query = 'I have some issues with payment'
category =['{"Category": "Billing"}']
response_type = step5.response_type(query, category)

print(response_type)



# Start speaking...
# WebSocket connection closed unexpectedly in sender: sent 1000 (OK); no close frame received
# final answer: {"Category": "FAQs"}

# Hello! Welcome to the Grand Holiday Hotel. Yes, we do have Wi-Fi available throughout the hotel. Would you like to know more about our internet connection or do you have any other questions?
# ['{"Category": "FAQs"}']
# Traceback (most recent call last):
#   File "main.py", line 17, in <module>
#     response_type = step5.response_type(query, category)
#   File "E:\Techhelps\v2v-p4\v4\step5.py", line 19, in response_type
#     if FAQ in category:
# TypeError: argument of type 'NoneType' is not iterable
