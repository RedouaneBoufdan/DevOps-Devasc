import requests
from config import BASE_URL, USERNAME, PASSWORD

book_id = 999

r = requests.delete(
    f"{BASE_URL}/books/{book_id}",
    auth=(USERNAME, PASSWORD),
    timeout=10
)

print("Status:", r.status_code)
print(r.text)
