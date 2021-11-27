from __future__ import print_function
import requests
import json

test_url = 'http://127.0.0.1:2020/bot'

question = 'Who are you?'
text_json = {'Body':question}
response = requests.post(test_url, json=text_json)

print(json.loads(response.text))