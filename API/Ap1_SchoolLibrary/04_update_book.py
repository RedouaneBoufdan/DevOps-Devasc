import requests
from config import BASE_URL, USERNAME, PASSWORD

book_id = 999
updated_book = {"id": 999, "title": "DevOps Exam Book (UPDATED)", "author": "Student"}

r = requests.put(
    f"{BASE_URL}/books/{book_id}",
    json=updated_book,
    auth=(USERNAME, PASSWORD),
    timeout=10
)

print("Status:", r.status_code)
print(r.text)
