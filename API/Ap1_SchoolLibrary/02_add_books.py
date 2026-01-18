import requests
from config import BASE_URL, API_KEY

headers = {
    "Content-Type": "application/json",
    "X-API-KEY": API_KEY
}

new_book = {
    "id": 11,
    "title": "teee",
    "author": "ttttt"
}

r = requests.post(
    f"{BASE_URL}/books",
    json=new_book,
    headers=headers,
    timeout=10
)

print("Status:", r.status_code)
print(r.text)
