'''
1. Maak een lijst met alleen even nummers
antwoord = [4, 8, 10]
'''
print('1.')

lijst = [1, 4, 5, 7, 8, 10, 11]
antwoord = []
for getal in lijst:
    if getal % 2 == 0:
        antwoord.append(getal)

print(antwoord)

# korte versie
print(list(filter(lambda x: x % 2 == 0, lijst)))
# of
print([x for x in lijst if x % 2 == 0])

'''
2. Tel alle cijfers in de lijst op
antwoord = 46
'''
print()
print ('2.')

lijst = [1, 4, 5, 7, 8, 10, 11]
antwoord = 0
for getal in lijst:
    antwoord = antwoord + getal
print(antwoord)

# korte versie
print (sum(lijst))

'''
3. Verwijder alle dubbele elementen uit een lijst. Het antwoord moet weer een lijst zijn
'''
print()
print ('3.')

lijst = ['x', 'a', 'b', 'a', 'a', 'x']
unieke_elementen = set(lijst)
antwoord = list(unieke_elementen)
print(antwoord)

'''
4. Vermenigvuldig alle getallen in een lijst met 2
'''
print()
print('4.')

lijst = [1, 4, 5, 7, 8, 10, 11]
antwoord = []
for getal in lijst:
    antwoord.append(getal*2)

print(antwoord)

# korte versie
print(list(map(lambda x: x * 2, lijst)))
# of
print([x * 2 for x in lijst])
