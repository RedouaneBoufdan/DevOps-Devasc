# Ap1 – School Library API (DEVASC VM)

## Doel
Het doel van dit experiment is het verkennen en testen van een REST API
(School Library API) die wordt aangeboden in de DEVASC VM.

## Omgeving
- DEVASC Virtual Machine
- School Library API
- Swagger (API documentatie)
- Python 3 + requests

## Base URL
http://library.demo.local/api/v1

## Authenticatie
De API gebruikt token-based authenticatie.

1. Login via `POST /loginViaBasic`
2. De API retourneert een **token**
3. Dit token wordt meegestuurd in de HTTP header:


X-API-KEY: <token>


## Gebruikte endpoints
- GET /books
- POST /books
- GET /books/{id}
- PUT /books/{id}
- DELETE /books/{id}
- POST /loginViaBasic
- POST /loginViaJSON

## Tests
### Swagger
- Authorize met X-API-KEY
- POST /books
- GET /books

### Python scripts
Dezelfde API-calls werden geautomatiseerd met Python (`requests`):
- 01_get_all_books.py
- 02_add_books.py
- 03_get_book_by_id.py
- 04_update_book.py
- 05_delete_book.py
- 06_login_basic.py
- 07_login_json.py

## Resultaat
- Succesvolle authenticatie met token
- CRUD-operaties op boeken via Swagger en Python
- Correcte HTTP status codes (200 / 201)

## Bewijs
Screenshots zijn beschikbaar in de map `screenshots/`.
