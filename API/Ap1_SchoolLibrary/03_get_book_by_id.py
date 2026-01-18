import requests
from config import BASE_URL

book_id = 44

r = requests.get(f"{BASE_URL}/books/{book_id}", timeout=10)
print("Status:", r.status_code)
print(r.text)
