# 1.
print()
print("1.")

woorden = ['noot', 'mies', 'tomatensoep', 'aap']
for woord in woorden:
    print(woord, ": ", len(woord))

# 2.
print()
print("2.")
#
# rechtoe-rechtaan versie:
#
woorden = ['noot', 'mies', 'tomatensoep', 'aap']
lengte_langste_woord = 0
index_langste_woord = None

for i in range(0, len(woorden)):
    woord = woorden[i]
    lengte_woord = len(woord)
    if lengte_woord > lengte_langste_woord:
        lengte_langste_woord = lengte_woord
        index_langste_woord = i

langste_woord = woorden[index_langste_woord]
print("langste woord: ", langste_woord)
print("lengte langste woord: ", len(langste_woord))

#
# kortere versie:
#
grootste_lengte = max(map(lambda woord: len(woord), woorden))
langste_woord = next(filter(lambda woord: len(woord) == grootste_lengte, woorden))
print ("langste woord: ", langste_woord)
print ("lengte langste woord: ", len(langste_woord))

# 3.
print()
print("3.")
cijfers = [1, 3, 5, 7, 9, 2]
#
# rechtoe-rechtaan versie:
#
hoogste_cijfer = None
for cijfer in cijfers:
    if hoogste_cijfer == None or hoogste_cijfer<=cijfer:
        hoogste_cijfer = cijfer

print ("hoogste cijfer: ", hoogste_cijfer)

#
# hiervoor is een standaard functie beschikbaar in Python:
hoogste_cijfer = max(cijfers)
print ("hoogste cijfer: ", hoogste_cijfer)

# 4.
print()
print("4.")

# input
hoogste_cijfer = [3, 5, 6, 10]
laagste_cijfer = [1, 2, 2, 9]
#
# rechtoe-rechtaan versie:
#
grootste_verschil = 0
index_grootste_verschil = None
for i in range(0, len(hoogste_cijfer)):
    verschil = hoogste_cijfer[i] - laagste_cijfer[i]
    if grootste_verschil<verschil:
        grootste_verschil = verschil
        index_grootste_verschil = i

print ("het grootste verschil tussen het hoogste en laagste cijfer is "
       , grootste_verschil, ". Dat is bij cijferpaar ("
       ,hoogste_cijfer[index_grootste_verschil], ",", laagste_cijfer[index_grootste_verschil], ").")

#
# kortere versie
#
paren = set(zip(hoogste_cijfer, laagste_cijfer))
grootste_verschil =  max(map(lambda paar: paar[0]-paar[1], paren))
paar_met_grootste_verschil = next(filter(lambda paar: paar[0]-paar[1]==grootste_verschil, paren))

print ("het grootste verschil tussen het hoogste en laagste cijfer is "
       , grootste_verschil, ". Dat is bij cijferpaar ("
       ,paar_met_grootste_verschil[0], ",", paar_met_grootste_verschil[1], ").")

'''
5. Maak een lijst met alleen even nummers
antwoord = [4, 8, 10]
'''
print()
print('5.')

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
6. Tel alle cijfers in de lijst op
antwoord = 46
'''
print()
print ('6.')

lijst = [1, 4, 5, 7, 8, 10, 11]
antwoord = 0
for getal in lijst:
    antwoord = antwoord + getal
print(antwoord)

# korte versie
print(sum(lijst))

'''
7. Verwijder alle dubbele elementen uit een lijst. Het antwoord moet weer een lijst zijn
'''
print()
print ('7.')

lijst = ['x', 'a', 'b', 'a', 'a', 'x']
unieke_elementen = set(lijst)
antwoord = list(unieke_elementen)
print(antwoord)

'''
8. Vermenigvuldig alle getallen in een lijst met 2
'''
print()
print('8.')

lijst = [1, 4, 5, 7, 8, 10, 11]
antwoord = []
for getal in lijst:
    antwoord.append(getal*2)

print(antwoord)

# korte versie
print(list(map(lambda x: x * 2, lijst)))
# of
print([x * 2 for x in lijst])

'''
9. Maak een dict van een lijst
'''
print()
print('9.')

lijst = [1, 2, 3, 4]

antwoord = {}

for x in lijst:
    antwoord[x] = x

print(antwoord)

# korte versie
print({x: x for x in lijst})

'''
10. Maak een dict van een lijst, de key is het element van de lijst, de value is het kwadraat van de key
'''
print()
print('10.')

lijst = [1, 2, 3, 4]

antwoord = {}

for x in lijst:
    antwoord[x] = x*x

print(antwoord)

# korte versie
print({x: x*x for x in lijst})

'''
11. Maak een dict van een lijst, de key is het element van de lijst, de value is het kwadraat van de key.
In het antwoord mogen alleen veelvouden van 4 voorkomen
'''
print()
print('11.')

lijst = [1, 2, 3, 4]

antwoord = {}

for x in lijst:
    kwadraad = x*x
    if kwadraad % 4 == 0:
        antwoord[x] = kwadraad

print(antwoord)

# korte versie
print({x: x*x for x in lijst if x*x % 4 == 0})

'''
12. Trek het kleinste getal in de lijst af van alle andere getallen
'''
print()
print('12.')

lijst = [10, 2, 3, 4, 6]

#
# rechtoe-rechtaan versie:
#
laagste_cijfer = None
for cijfer in lijst:
    if laagste_cijfer == None or laagste_cijfer > cijfer:
        laagste_cijfer = cijfer

antwoord = []
for cijfer in lijst:
        antwoord.append(cijfer - laagste_cijfer)

print (antwoord)

# korte versie
laagste_cijfer = min(lijst)
print(list(x - laagste_cijfer for x in lijst))

'''
13. Tel hoe vaak een woord voorkomt in een lijst
'''
print()
print('13.')

lijst = ['woord1', 'woord1', 'woord2', 'woord1', 'woord3', 'woord3']
antwoord = {}

for woord in lijst:
    aantal = antwoord.get(woord)
    if aantal == None:
        aantal = 0
    aantal = aantal + 1
    antwoord[woord] = aantal

print(antwoord)

'''
14. Controleer of een lijst gesorteerd is. 
'''
print()
print('14.')

lijst_gesorteerd = [1, 3, 5, 7] # True
gesorteerd = True
vorig_cijfer = None
for cijfer in lijst_gesorteerd:
    if vorig_cijfer is None:
        vorig_cijfer = cijfer
    elif cijfer < vorig_cijfer:
        gesorteerd = False

print(gesorteerd)

lijst_niet_gesorteerd = [3, 5, 1, 7] # False
gesorteerd = True
vorig_cijfer = None
for cijfer in lijst_niet_gesorteerd:
    if vorig_cijfer is None:
        vorig_cijfer = cijfer
    elif cijfer < vorig_cijfer:
        gesorteerd = False

print(gesorteerd)

# Korte(re) versie
def is_deze_lijst_gesorteerd(lijst):
    vorig_cijfer = None
    for cijfer in lijst:
        if vorig_cijfer is None:
            vorig_cijfer = cijfer
        elif cijfer < vorig_cijfer:
            return False
    return True


print(is_deze_lijst_gesorteerd(lijst_gesorteerd))
print(is_deze_lijst_gesorteerd(lijst_niet_gesorteerd))

'''
15. Controleer of alle cijfers in een lijst groter zijn dan 10 
'''
print()
print('15.')

lijst_kleine_cijfers = [1, 3, 5, 7]  # False
lijst_grote_cijfers = [14, 15]  # True

def zijn_alle_cijfers_groter_dan_10(lijst):
    for cijfer in lijst:
        if cijfer <= 10:
            return False
    return True


print(zijn_alle_cijfers_groter_dan_10(lijst_kleine_cijfers))
print(zijn_alle_cijfers_groter_dan_10(lijst_grote_cijfers))

# korte versie
import functools
print(functools.reduce(lambda x, y: x & (y > 10), lijst_kleine_cijfers, True))
print(functools.reduce(lambda x, y: x & (y > 10), lijst_grote_cijfers, True))

'''
16. Pas de oplossing in 11 aan zodat je ipv 10 een andere grens kunt kiezen
'''
print()
print('16.')

lijst_kleine_cijfers = [1, 3, 5, 7]  # False
lijst_grote_cijfers = [14, 15]  # True

def zijn_alle_cijfers_groter_dan_X(lijst, x):
    for cijfer in lijst:
        if cijfer <= x:
            return False
    return True


print(zijn_alle_cijfers_groter_dan_X(lijst_kleine_cijfers, 10))
print(zijn_alle_cijfers_groter_dan_X(lijst_grote_cijfers, 10))
