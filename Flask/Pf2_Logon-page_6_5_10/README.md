# Pf2 – Logon-page experiment (Lab 6.5.10)

## Beschrijving
In deze lab heb ik een eenvoudige webapplicatie gemaakt met **Python en Flask**.  
De applicatie toont de evolutie van wachtwoordbeveiliging:
- opslag van wachtwoorden in **platte tekst**
- opslag van wachtwoorden met **hashing (SHA256)**

De gebruikersgegevens worden opgeslagen in een **SQLite-database**.

---

## Doel van de lab
- Begrijpen waarom platte tekst onveilig is  
- Leren hoe hashing wachtwoorden beter beschermt  
- Het verschil zien tussen plaintext en hash in de database

---

## Resultaat
- In de tabel `USER_PLAIN` zijn wachtwoorden leesbaar  
- In de tabel `USER_HASH` zijn wachtwoorden gehasht  
- Gebruikers met hetzelfde wachtwoord hebben hetzelfde hash (geen salt)

---

## Gebruikte commando’s

### Installatie
```bash
pip3 install flask
pip3 install pyotp

Applicatie starten
nohup python3 password-evolution.py &

Server stoppen
pkill -f password-evolution.py


Plain text gebruikers aanmaken
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' https://0.0.0.0:5000/signup/v1
curl -k -X POST -F 'username=bob' -F 'password=passwordforbob' https://0.0.0.0:5000/signup/v1

Plain text login
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' https://0.0.0.0:5000/login/v1

Hash gebruikers aanmaken
curl -k -X POST -F 'username=rick' -F 'password=samepassword' https://0.0.0.0:5000/signup/v2
curl -k -X POST -F 'username=allan' -F 'password=samepassword' https://0.0.0.0:5000/signup/v2
curl -k -X POST -F 'username=dave' -F 'password=differentpassword' https://0.0.0.0:5000/signup/v2

Hash login
curl -k -X POST -F 'username=rick' -F 'password=samepassword' https://0.0.0.0:5000/login/v2
