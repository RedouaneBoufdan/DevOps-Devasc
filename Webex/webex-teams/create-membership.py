# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests
import json

access_token = 'YTZhMTgwMDktNGNjZi00Nzg0LTljNmItZmQyYjg5ZTMzNTgxNGI0Zjk3NjAtYmZj_PE93_56361a18-ee8a-4da6-a728-ee9b2cd9887b'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZWNhNGIxMzAtZjRmMC0xMWYwLThlYWYtYjdiZDE1N2YwZGY3'
person_email = 'redouane.boufdan@student.odisee.be'

url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}

res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))
