# A2 – Eigen Ansible playbook-experiment (webserver via SSH)

In dit experiment gebruik ik Ansible om via SSH automatisch een webserver te installeren en te configureren.

## Doel van het experiment
- Verbinden met een host via Ansible inventory (192.0.2.3).
- Apache webserver installeren met Ansible.
- Een eenvoudige webpagina deployen.
- De webserver starten en beheren via Ansible.

## Opzet
Dit experiment is gebaseerd op de Ansible principes uit de cursus en sluit aan bij
infrastructure automation en application deployment.

## Bestanden
- `hosts` – Inventory file met de webserver (192.0.2.3) en SSH-credentials.
- `ansible.cfg` – Lokale Ansible configuratie (inventory, geen host key checking).
- `a2_webserver.yml` – Ansible playbook voor installatie en configuratie van Apache.

## Werking
Het playbook voert de volgende stappen uit:
1. Installeert Apache2 via het apt-module.
2. Activeert de benodigde Apache modules.
3. Plaatst een aangepaste `index.html` pagina.
4. Start en activeert de Apache service.

## Testen
1. Start de SSH-service op de VM:
   
   sudo systemctl start ssh
2. Test de connectiviteit:

    ansible webservers -m ping

3. Run het playbook:

    ansible-playbook a2_webserver.yml

4. Open de webpagina in de browser:

    http://192.0.2.3:8081

Resultaat

Na uitvoering van het playbook is de Apache webserver bereikbaar op poort 8081
en toont deze een webpagina die automatisch door Ansible werd gedeployed