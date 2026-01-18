# Dm1 – Docker management experiment

## Task name
Dm1 – Docker Management

## Task preparation
Voor dit experiment gebruik ik een bestaande Docker image (`di1-micro-web`).
Docker Desktop is actief en werkt via WSL2.

## Task implementation
Ik heb een container gestart en verschillende Docker management commando’s uitgevoerd:
- docker images
- docker ps
- docker inspect
- docker stats
- docker exec
- docker stop
- docker rm

## Task troubleshooting
Tijdens het experiment heb ik gecontroleerd of de container correct draaide en of de juiste poorten gemapt waren.
Er waren geen grote problemen.

## Task verification
- In `docker ps` stond de container op status **Up**
- Met `docker inspect` kon ik de configuratie en IP-adres zien
- Met `docker stats` zag ik live resource usage
- Met `docker exec` kon ik in de container werken
- De container werd correct gestopt en verwijderd

Screenshots zijn toegevoegd in deze map.
