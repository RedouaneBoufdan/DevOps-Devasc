# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests
import json

access_token = 'YTZhMTgwMDktNGNjZi00Nzg0LTljNmItZmQyYjg5ZTMzNTgxNGI0Zjk3NjAtYmZj_PE93_56361a18-ee8a-4da6-a728-ee9b2cd9887b'

url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    'title': 'DevOps Exam Room - Redouane'
}

res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))
