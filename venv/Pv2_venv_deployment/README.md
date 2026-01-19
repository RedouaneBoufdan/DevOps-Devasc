# Pv2 – Eigen venv-experiment (deployment)

In dit experiment gebruik ik een Python virtual environment voor een eenvoudige deployment.

## Doel
- Een applicatie runnen in een geïnstalleerde virtual environment.
- Dependencies beheren met pip en requirements.txt.
- Een eenvoudige Flask-app deployen.

## Bestanden
- `app.py` – Flask applicatie.
- `requirements.txt` – Python dependencies.

## Stappen
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py

Resultaat

De Flask applicatie draait in een virtual environment en is bereikbaar via http://localhost:5000