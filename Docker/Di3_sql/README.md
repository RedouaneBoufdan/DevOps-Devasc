# Di3 – Eigen image-experiment 2 (SQL)

## Beschrijving
In deze oefening heb ik een **SQL-database** uitgevoerd in een **Docker container** met **PostgreSQL**.  
De database draait in een container en gebruikt een **Docker volume** om data persistent op te slaan.

---

## Doel
- Werken met een SQL-database in Docker  
- Gebruik maken van environment variables  
- Data persistent opslaan met een Docker volume  
- Controleren van data via SQL-commando’s

---

## Resultaat
- PostgreSQL draait in een Docker container  
- Een tabel `notes` is aangemaakt  
- Data blijft bestaan na het stoppen en opnieuw starten van de container  
- Toegang tot de database via `psql`

---

## Gebruikte commando’s

### Docker volume aanmaken
```bash
docker volume create di3_pgdata

PostgreSQL container starten

docker run -d --name di3-postgres \
  -e POSTGRES_USER=devasc \
  -e POSTGRES_PASSWORD=devasc \
  -e POSTGRES_DB=labdb \
  -p 5432:5432 \
  -v di3_pgdata:/var/lib/postgresql/data \
  -v "$PWD/init.sql":/docker-entrypoint-initdb.d/init.sql:ro \
  postgres:16

Controleren of de container draait

docker ps
docker logs di3-postgres

SQL-commando’s uitvoeren

docker exec -it di3-postgres psql -U devasc -d labdb -c "\dt"
docker exec -it di3-postgres psql -U devasc -d labdb -c "SELECT * FROM notes;"

Data toevoegen

docker exec -it di3-postgres psql -U devasc -d labdb \
  -c "INSERT INTO notes(msg) VALUES ('persistent test');"

Container stoppen en verwijderen

docker stop di3-postgres
docker rm di3-postgres

Container opnieuw starten (met hetzelfde volume)

docker run -d --name di3-postgres \
  -e POSTGRES_USER=devasc \
  -e POSTGRES_PASSWORD=devasc \
  -e POSTGRES_DB=labdb \
  -p 5432:5432 \
  -v di3_pgdata:/var/lib/postgresql/data \
  postgres:16
