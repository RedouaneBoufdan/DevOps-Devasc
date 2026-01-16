# Di1 – Lab 6.2.7 Flask Microweb App in Docker

## Taaknaam
Docker – Flask microservice (Lab 6.2.7)

## Taakvoorbereiding
Voor deze taak heb ik Docker Desktop geïnstalleerd met WSL2 ondersteuning.
Daarnaast heb ik een werkende Flask applicatie voorbereid met HTML templates en CSS bestanden.
De bronbestanden bevinden zich in één map met een Dockerfile.

## Taakimplementatie
Ik heb een Docker image gebouwd op basis van een Python image.
In de Dockerfile wordt Flask geïnstalleerd en worden de applicatiebestanden
(flask_app.py, templates en static) gekopieerd naar de container.

Daarna heb ik de Docker image gebouwd met het commando:

docker build -t microweb_image .

Vervolgens heb ik een container gestart met port mapping van poort 5050:

docker run -d -p 5050:5050 --name di1-running microweb_image

De Flask applicatie draait in de container en luistert op alle interfaces (0.0.0.0).

## Taakproblemen en oplossingen
In het begin werkte Docker niet in WSL omdat Docker Desktop niet geactiveerd was
voor WSL2. Dit probleem werd opgelost door WSL-integratie te activeren in
Docker Desktop instellingen.

Daarnaast moest ik controleren of de juiste poorten werden gemapt
tussen host en container.

## Taakverificatie
De containerstatus werd gecontroleerd met:

docker ps

De logs van de container tonen dat de Flask server correct draait:

docker logs di1-running

De applicatie is bereikbaar via de browser op:
http://127.0.0.1:5050

De webpagina toont correct de Flask output met CSS styling,
wat bewijst dat de container correct functioneert.
