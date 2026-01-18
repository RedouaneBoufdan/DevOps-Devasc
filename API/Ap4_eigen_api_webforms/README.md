# Ap4 – Eigen API-experiment 2 (Python) (webforms)

In dit experiment heb ik een kleine Flask-webapp gemaakt met een webformulier.
De gebruiker kiest een categorie en klikt op een knop om data op te halen via een REST API.

## Wat gebeurt er?
- De webpagina toont een dropdown (categorie) en een knop **Get Joke**.
- Bij submit stuurt Flask een request naar een publieke REST API.
- De JSON-response wordt verwerkt en de tekst wordt getoond op de webpagina.

## Bestanden
- `app.py` – Flask-app die de form verwerkt en de API oproept.
- `templates/index.html` – HTML webform en output.
- `requirements.txt` – dependencies (flask, requests).

## Runnen / testen
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 app.py
