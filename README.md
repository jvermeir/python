# Opdrachten met Python

Deze repo bevat oefenmateriaal voor Python opdrachten. 

## Algemene aanpak

Een oplossing ziet er altijd ongeveer zo uit:

1. Bepaal de vorm van het antwoord, dwz is het antwoord een getal, een lijst, een dict, of nog iets anders? Definieer dan een variabele waarin straks het antwoord komt te staan. Dus:
```
antwoord = 0
antwoord = None
antwoord = []
```
2. Schrijf de oplossing, in deze opdrachten kan dat altijd met een `for` loop op de lijst die bij de vraag hoort:
```
for getal in lijst:
  # doe iets slims
```
In de for loop krijgt antwoord de uiteindelijke waarde. Dat kan door iets toe te voegen aan een lijst of een dict. Of door er 1 bij op te tellen. 
```
for getal in lijst:
    antwoord.append(getal*2)
```
3. Print nu het resultaat:
```
print(antwoord)
```

### Alternatieven

In Python kun je ook een functie rechtstreeks uitvoeren op een verzameling. Een verzameling kan een list, een set of een dict zijn. 
Daarmee kun je vaak kortere oplossingen maken. Deze regel doet hetzelfde als de for-lus hierboven:
```
antwoord = [x * 2 for x in lijst]
```

