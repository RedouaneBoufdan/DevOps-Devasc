import requests
from config import BASE_URL

r = requests.get(f"{BASE_URL}/books", timeout=10)
print("Status:", r.status_code)
print(r.text)
