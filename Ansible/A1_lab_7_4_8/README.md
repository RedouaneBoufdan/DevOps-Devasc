# Apache Webserver Automatisering met Ansible

## Beschrijving
Dit project gebruikt **Ansible** om automatisch een **Apache2 webserver** te installeren en te configureren op een Ubuntu-systeem.

De webserver wordt ingesteld om te luisteren op **poort 8081** in plaats van de standaardpoort 80.

## Vereisten
- Ubuntu (DEVASC VM)
- Ansible
- SSH geactiveerd
- Internetverbinding

## Gebruikte IP
- Webserver: `192.0.2.3`
- Poort: `8081`

## Belangrijkste stappen
1. Ansible configureren met een inventory en configbestand  
2. Verbinding testen met een ping-playbook  
3. Apache2 automatisch installeren via een playbook  
4. Apache configureren om poort 8081 te gebruiken  

## Resultaat
Na uitvoering van het playbook is de Apache webserver bereikbaar via:  
`http://192.0.2.3:8081`

De standaard Apache2 Ubuntu-pagina wordt correct weergegeven.

## Apache stoppen/starten
De webserver kan worden gestopt/start met het volgende commando:

sudo systemctl stop apache2

sudo systemctl status apache2

sudo systemctl start apache2
