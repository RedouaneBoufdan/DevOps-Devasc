# Ap3 – Eigen API-experiment (Python)

In dit experiment toon ik hoe ik een publieke REST API gebruik in Python.

## Wat doet dit script?
Het script stuurt een **GET request** naar de Chuck Norris Jokes API en ontvangt een JSON-response.
Daarna leest het script enkele velden uit de JSON (zoals `value`, `id`, `created_at`) en toont het resultaat in de terminal.

## Bestand
- `chuck_norris_api.py` – Python script dat de API oproept en JSON verwerkt.

## Hoe testen?
1. Installeer dependency (indien nodig):
   ```bash
   pip3 install requests
