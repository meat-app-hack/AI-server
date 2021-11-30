from __future__ import print_function
import requests
import json
import base64

url = 'https://firebasestorage.googleapis.com/v0/b/message-app-dfc81.appspot.com/o/images%2F1046769.png?alt=media&amp;token=ffa4286a-8ef4-43be-8599-42b5bb1b5f4f'
test_url = 'http://127.0.0.1:2020/predict'

img_json = {'passbase64str':url}
response = requests.post(test_url, json=img_json)

print(response)
print(json.loads(response.text))