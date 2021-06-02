# Train-Everywhere
https://github.com/M0nt3M4t3/Train-Everywhere

## Medlemmar:
- Carl Montelius
- Caroline Kristensen
- Cassandra Windahl
- Felicia Bergflo
- Filip Kroon

## Hur man öppnar upp webbsidan:

1. Öppna upp din terminal på datorn och skriv in följande: pip install bottle
OBS! Vid Mac kan du ibland ha Python 2 installerat också så skriv då: pip3 install bottle

2. Skapa databasen genom att köra alla queurys du finner i Querys.docx
i MySQL.

3. För att programmet ska kunna köras med MySQL behövs även MySQL-connector. I terminalen skriv: pip3 install mysql-connector-python

4. Öppna upp hela mappen "Projektarbete" i Visual Studio Code.

5. Skapa en pythonfil som heter "safety.py"

6. Safety.py ska ha innehåll enligt följande: 
info = ['root', '"Ditt lösenord"', 'localhost', 'Train_Everywhere']
(Ändra "Ditt lösenord" till ditt lösenord på MySQL)

7. Ändra password till ditt lösenord till databashanteraren.

8. Gå in på visual och starta servern genom att välja python filen ”project.py” och starta den. 

9. Gå sedan in på en webbläsare och skriv: http://127.0.0.1:8000/ och sök. 

10. Nu bör du se vår hemsida på din webbläsare.
