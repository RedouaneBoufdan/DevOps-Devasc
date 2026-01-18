# Ap6 – Eigen REST-API experiment met curl (forms)

In dit experiment gebruik ik `curl` om een HTTP POST request te sturen met formulierdata.

## Wat doet dit experiment?
- Met `curl` stuur ik een POST request naar een test REST API.
- Ik verzend formuliergegevens met de optie `-d`.
- De API stuurt een JSON-response terug met de ontvangen data.

Dit experiment toont het verschil tussen een GET en een POST request.

## Gebruikte commando's

curl -X POST https://httpbin.org/post \
     -d "name=student" \
     -d "course=devops"

curl -X POST https://httpbin.org/post \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "name=student" \
     -d "course=devops"
