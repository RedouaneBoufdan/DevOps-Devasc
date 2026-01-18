import requests
from config import BASE_URL, USERNAME, PASSWORD

r = requests.post(
    f"{BASE_URL}/loginViaBasic",
    auth=(USERNAME, PASSWORD),
    timeout=10
)

print("Status:", r.status_code)
print(r.json())
