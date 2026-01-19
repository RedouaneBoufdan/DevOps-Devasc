import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "474b61d8-aeaa-4863-828f-78d325bcf13a" 

url = geocode_url + urllib.parse.urlencode({"q": loc1, "limit": "1", "key": key})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

print(json_data)
