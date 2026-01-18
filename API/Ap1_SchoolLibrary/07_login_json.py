import requests
from config import BASE_URL, USERNAME, PASSWORD

payload = {"username": USERNAME, "password": PASSWORD}

r = requests.post(
    f"{BASE_URL}/loginViaJSON",
    json=payload,
    timeout=10
)

print("Status:", r.status_code)
print(r.text)
