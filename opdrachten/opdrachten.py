'''
oefeningen met lijsten en loops

algemeen algorithme:

1. definieer een of meer variabelen waarin het eindresultaat opgeslagen wordt.
2. bekijk elk element van de lijst en bepaal of je het eindresultaat aan moet passen
3. print het eindresultaat
'''

# 1.
# input
woorden = ['noot', 'mies', 'tomatensoep', 'aap']
'''
vraag:
    print elk woord en de lengte er van op aparte regels
resultaat:
    noot: 4
    mies: 4
    tomatensoep: 11 
    aap: 3

bonusvraag: 
    wat gebeurt er als woorden gelijk is aan de lege lijst?
    wat gebeurt er als woorden de waarde None heeft?
'''

# 2.
# input
woorden = ['noot', 'mies', 'tomatensoep', 'aap']
'''
vraag:
    wat is de lengte van het langste woord?
    wat is het langste woord?
resultaat:
'''
lengte_langste_woord = 11
langste_woord = 'tomatensoep'

# 3.
# input
cijfers = [1, 3, 5, 7, 9, 2]
'''    
vraag:
    wat is het hoogste cijfer
resultaat:
'''
het_hoogste_cijfer = 9

# 4.
# input
hoogste_cijfer = [3, 5, 6, 10]
laagste_cijfer = [1, 2, 2, 9]
'''
vraag:
    wat is het grootste verschil tussen twee paren van hoogste_cijfer/laagste_cijfer?
    alle hoogste/laagste paren zijn:
    (3,1) (5,2) (6,2) (10,9)
resultaat:
'''
het_grootste_verschil = 4
'''
bonusvraag:
    wat gebeurt er als de ene lijst langer is dan de andere?
'''

'''
Maak 2 oplossingen:
- gebruik alleen loops over lijsten.
- extra: gebruik standaard Python functies zoals sum() en filter()
'''

'''
5. Maak een lijst met alleen even nummers
input
'''
lijst = [1, 4, 5, 7, 8, 10, 11]

antwoord = [4, 8, 10]

'''
6. Tel alle cijfers in de lijst op
input
'''

lijst = [1, 4, 5, 7, 8, 10, 11]

antwoord = 46

'''
7. Verwijder alle dubbele elementen uit een lijst. Het antwoord moet weer een lijst zijn.
input
'''
lijst = ['x', 'a', 'b', 'a', 'a', 'x']

antwoord = ['a', 'b', 'x']

'''
8. Vermenigvuldig alle getallen in een lijst met 2
'''
lijst = [1, 4, 5, 7, 8, 10, 11]
antwoord = [2, 8, 10, 14, 16, 20, 22]

'''
9. Maak een dict van een lijst
'''
lijst = [1, 2, 3, 4]
antwoord = {1: 1, 2: 2, 3: 3, 4: 4}

'''
10. Maak een dict van een lijst, de key is het element van de lijst, de value is het kwadraat van de key
'''
lijst = [1, 2, 3, 4]
antwoord = {1: 1, 2: 4, 3: 9, 4: 16}

'''
11. Maak een dict van een lijst, de key is het element van de lijst, de value is het kwadraat van de key.
In het antwoord mogen alleen veelvouden van 4 voorkomen
'''
lijst = [1, 2, 3, 4]
antwoord = {2: 4, 4: 16}

'''
12. Trek het kleinste getal in de lijst af van alle getallen in de lijst.
hint: combineer 2 stappen:
- zoek eerst het kleinste getal
- trek daarna het kleinste getal af van de andere getallen. 
'''
lijst = [10, 2, 3, 4, 6]
antwoord = [8, 0, 1, 2, 4]

'''
13. Tel hoe vaak een woord voorkomt in een lijst
'''
lijst = ['woord1', 'woord1', 'woord2', 'woord1', 'woord3', 'woord3']
antwoord = {{'woord1': 3}, {'woord2': 1}, {'woord3':2}}

'''
14. Controleer of een lijst gesorteerd is. 
'''
lijst_gesorteerd = [1, 3, 5, 7] # True
lijst_niet_gesorteerd = [3, 5, 1, 7] # False

'''
15. Controleer of alle cijfers in een lijst groter zijn dan 10 
'''
lijst_kleine_cijfers = [1, 3, 5, 7]  # False
lijst_grote_cijfers = [14, 15]  # True

'''
16. Pas de oplossing in 15 aan zodat je ipv 10 een andere grens kunt kiezen
'''
lijst_kleine_cijfers = [1, 3, 5, 7]  # False
lijst_grote_cijfers = [14, 15]  # True

'''
17. Print alle combinaties van elementen in lijst a en lijst b
Je hebt twee for loops in elkaar nodig
'''
lijst_a = ['a1', 'a2', 'a3']
lijst_b = ['b1', 'b2', 'b3']
antwoord = ['a1b1', 'a1b2', 'a1b3', 'a2b1', 'a2b2', 'a2b3', 'a3b1', 'a3b2', 'a3b3']

'''
18. Print 'even' voor elk even getal en 'oneven' voor elk oneven getal in de lijst.
Print ook het totale aantal even en oneven getallen.
'''
lijst = [1, 3, 2, 5, 8, 6, 11]
'''
output is
oneven
oneven
even
oneven
even
even
oneven
aantal even getallen:  3
aantal oneven getallen:  4
'''

'''
19. Maak een lijst met de som van alle paren van twee opeenvolgende getallen in de lijst.
Je hebt een while nodig ipv een for:

    i = 0
    while i<len(lijst):
        # do iets ...
        
Wat gebeurt er als de lijst een oneven aantal getallen bevat?
'''
lijst = [1, 3, 2, 5, 8, 6, 11]
antwoord = [4, 7, 14, 11]
