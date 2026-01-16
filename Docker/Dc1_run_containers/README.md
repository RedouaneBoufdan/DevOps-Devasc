# Dc1 – Run containers experiment

## Task name
Dc1 – Docker Run Containers

## Task preparation
Voor deze oefening gebruik ik een bestaande Docker image (di1-micro-web) van het vorige experiment (Di1).
Docker Desktop is actief en werkt via WSL2.

## Task implementation
Ik heb een container gestart met port mapping en daarna de werking gecontroleerd met docker commando’s.

Commando’s:
- docker run -d -p 8080:5050 --name di1-running di1-micro-web
- docker ps
- docker logs di1-running
- docker stop di1-running
- docker rm di1-running

## Task troubleshooting
Ik controleerde de port mapping (host 8080 naar container 5050) omdat de webapp anders niet bereikbaar is.

## Task verification
- In `docker ps` staat de container op status **Up**.
- In `docker logs` is te zien dat Flask correct draait en dat HTTP requests (GET) worden verwerkt.
- De container werd daarna netjes gestopt en verwijderd (stop + rm).

Screenshots staan in de map `screenshots/`.
