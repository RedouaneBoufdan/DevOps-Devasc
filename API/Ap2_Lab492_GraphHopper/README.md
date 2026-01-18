# GraphHopper REST API Integratie – Python

Dit project laat zien hoe je de GraphHopper REST API gebruikt in een Python-programma.  
De applicatie haalt locatiegegevens op, berekent een route tussen twee plaatsen en toont afstand, reistijd en routebeschrijvingen.

Het project is stap voor stap opgebouwd volgens de Cisco lab-instructies.  
Elk Python-bestand stelt één fase van de ontwikkeling voor.

## Beschrijving van de bestanden

- **graphhopper_parse-json_1.py**  
  Test de Geocoding API en toont de ruwe JSON-gegevens.

- **graphhopper_parse-json_2.py**  
  Voegt een geocoding-functie toe om latitude en longitude op te halen.

- **graphhopper_parse-json_3.py**  
  Laat de gebruiker een startlocatie en bestemming invoeren.

- **graphhopper_parse-json_4.py**  
  Behandelt fouten zoals lege invoer, ongeldige locaties en API-fouten.

- **graphhopper_parse-json_5.py**  
  Gebruikt de Routing API om afstand en reistijd te berekenen.

- **graphhopper_parse-json_6.py**  
  Toont stap-voor-stap route-instructies.

- **graphhopper_parse-json_7.py**  
  Eindversie met keuze van vervoermiddel (auto, fiets, te voet) en volledige foutafhandeling.
