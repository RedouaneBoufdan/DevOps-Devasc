# A3 – Eigen Ansible playbook-experiment (andere server via SSH)

In dit experiment gebruik ik Ansible om een andere serverdienst te installeren en te beheren via SSH.

## Doel van het experiment
- Verbinden met een host via SSH (192.0.2.3).
- Installeren van een andere serverdienst dan Apache.
- Automatisch starten en activeren van de service.

## Gebruikte server
Voor dit experiment werd gekozen voor de nginx webserver als alternatieve serverdienst.

## Bestanden
- `hosts` – Inventory file met de doelhost (192.0.2.3).
- `ansible.cfg` – Lokale Ansible configuratie.
- `a3_nginx.yml` – Ansible playbook voor installatie en beheer van nginx.

## Werking
Het playbook voert de volgende stappen uit:
1. Installeert nginx via het apt-module.
2. Start de nginx service.
3. Activeert nginx bij het opstarten van het systeem.

## Testen

ansible-playbook a3_nginx.yml

Na uitvoering is de nginx webserver bereikbaar via:

http://192.0.2.3

De standaard nginx welkomstpagina bevestigt een succesvolle installatie.