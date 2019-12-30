'''
Opdrachten met lijsten
Maak 2 oplossingen:
- gebruik alleen loops over lijsten.
- extra: gebruik standaard Python functies zoals sum() en filter()
'''

'''
1. Maak een lijst met alleen even nummers
input
'''
lijst = [1, 4, 5, 7, 8, 10, 11]

antwoord = [4, 8, 10]

'''
2. Tel alle cijfers in de lijst op
input
'''

lijst = [1, 4, 5, 7, 8, 10, 11]

antwoord = 46

'''
3. Verwijder alle dubbele elementen uit een lijst. Het antwoord moet weer een lijst zijn.
input
'''
lijst = ['x', 'a', 'b', 'a', 'a', 'x']

antwoord = ['a', 'b', 'x']

'''
4. Vermenigvuldig alle getallen in een lijst met 2
'''
print()
print('4.')

lijst = [1, 4, 5, 7, 8, 10, 11]

antwoord = [2, 8, 10, 14, 16, 20, 22]

'''
5. Maak een dict van een lijst
'''
print()
print('5.')

lijst = [1, 2, 3, 4]

antwoord = {1: 1, 2: 2, 3: 3, 4: 4}

'''
6. Maak een dict van een lijst, de key is het element van de lijst, de value is het kwadraat van de key
'''
print()
print('6.')

lijst = [1, 2, 3, 4]

antwoord = {1: 1, 2: 4, 3: 9, 4: 16}

'''
7. Maak een dict van een lijst, de key is het element van de lijst, de value is het kwadraat van de key.
In het antwoord mogen alleen veelvouden van 4 voorkomen
'''
print()
print('7.')

lijst = [1, 2, 3, 4]

antwoord = {2: 4, 4: 16}

'''
8. Trek het kleinste getal in de lijst af van alle getallen in de lijst.
hint: combineer 2 stappen:
- zoek eerst het kleinste getal
- trek daarna het kleinste getal af van de andere getallen. 
'''
print()
print('8.')

lijst = [10, 2, 3, 4, 6]

antwoord = [8, 0, 1, 2, 4]

'''
9. Tel hoe vaak een woord voorkomt in een lijst
'''
print()
print('9.')

lijst = ['woord1', 'woord1', 'woord2', 'woord1', 'woord3', 'woord3']

antwoord = {{'woord1': 3}, {'woord2': 1}, {'woord3':2}}

'''
10. Controleer of een lijst gesorteerd is. 
'''
print()
print('10.')

lijst_gesorteerd = [1, 3, 5, 7] # True
lijst_niet_gesorteerd = [3, 5, 1, 7] # False


