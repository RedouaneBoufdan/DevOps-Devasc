(U1 – Lab 3.5.7 Unittest)
Doel

In dit experiment heb ik geleerd hoe ik Python unittest gebruik om een functie automatisch te testen. Het doel is om fouten sneller te vinden en code betrouwbaarder te maken.

Wat heb ik gedaan?

Ik heb een Python functie json_search() getest die recursief in een JSON-object zoekt naar een bepaalde key.

Ik heb een testbestand gemaakt met unittest.TestCase en drie tests:

een bestaande key moet gevonden worden (resultaat mag niet leeg zijn)

een niet-bestaande key mag niets opleveren (lege lijst)

de functie moet altijd een list teruggeven

Problemen en oplossing

Tijdens het testen vond ik een bug: de functie gaf eerst een lege lijst terug, ook wanneer de key wél bestond.
Ik heb dit opgelost door de functie te refactoren met een inner function en een lokale lijst ret_val, zodat resultaten correct worden opgebouwd en er geen ongewenste globale state is.

Resultaat

Alle unit tests slagen met:

python3 -m unittest -v
