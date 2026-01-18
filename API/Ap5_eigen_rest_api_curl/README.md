# Ap5 – Eigen REST-API experiment met curl

In dit experiment toon ik hoe ik een REST API kan testen met het command line tool `curl`.

## Wat doet dit experiment?
- Met `curl` stuur ik een HTTP GET request naar een publieke REST API.
- De API stuurt een JSON-response terug.
- De JSON-data wordt rechtstreeks getoond in de terminal.

Dit experiment toont dat een REST API ook getest kan worden zonder Python of een webapp.

## Gebruikte commando's

curl https://api.chucknorris.io/jokes/random

curl -X GET https://api.chucknorris.io/jokes/random

curl -i https://api.chucknorris.io/jokes/random
