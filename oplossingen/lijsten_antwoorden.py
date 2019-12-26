# 1.
print ("#1")

woorden = ['noot', 'mies', 'tomatensoep', 'aap']
for woord in woorden:
    print(woord, ": ", len(woord))

# 2.
print ("#2")
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
print ("#3")
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
print ("#4")
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
