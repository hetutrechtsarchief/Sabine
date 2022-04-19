# SABINE

SABINE, een voormalige bibliografie met literatuur over de geschiedenis van de provincie en stad Utrecht.

SABINE kwam voort uit een samenwerkingsverband tussen verschillende bibliotheken en erfgoedinstellingen. In het kader van deze samenwerking, die rond 2016 is beëindigd, zijn vele publicaties gedigitaliseerd.

Voor wie wil zoeken naar literatuur over de provincie en stad Utrecht verwijzen we naar de bibliotheekcatalogus van Het Utrechts Archief. Hierin zijn ook de links te vinden naar de publicaties die ten tijde van SABINE zijn gedigitaliseerd. 

https://hetutrechtsarchief.nl/onderzoek/resultaten/bibliotheek-mais


## Script

Deze Git repository bevat het Python script waarmee de titels in Sabine (met link: ±8.000 van de in totaal ±36.000) op basis van titel, auteur, paginanummer(s) en jaar van uitgave zijn gematcht op de lijst met 22.214 artikelen in de bibliotheek van het Utrechts Achief. 

* main.py

# Input

Beide lijsten zitten ook in deze repository en zijn beschikbaar als open data.

* sabine-tbl01.csv
* hua-artikelen.csv

## Resultaat

De spreadsheet afkomstig uit het script bevat fuzzy matches tussen de 2 lijsten met als doel om de ±8000 links uit Sabine te koppelen aan de artikelen bij HUA. De lijst wordt nog nagekeken alvorens de links worden geïmporteerd in het collectiebeheersysteem.

* HUA-Sabine-Fuzzy-Matches-score-vanaf-50pct-19-april-2022.xlsx


