'''
1. Maak een functie die alle cijfers in een lijst optelt
'''

lijst = [1, 4, 5, 7, 8, 10, 11]


def som(lijst):
    totaal = 0
    for getal in lijst:
        totaal = totaal + getal
    return getal


print ("het totaal is: ", som(lijst))

'''
2. Maak een functie die het laagste getal in een lijst bapaalt.
'''
lijst = [1, 4, 5, 7, 8, 10, 11]


def minimum(lijst):
    voorlopig_minimum = lijst[0]
    for getal in lijst:
        if getal < voorlopig_minimum:
            voorlopig_minimum = getal
    return voorlopig_minimum


print("het laagste getal is: ", minimum(lijst))
# ouput = 1

'''
3. Maak een functie die een getal bij elk getal in een lijst optelt.
'''

lijst = [1, 4, 5, 7, 8, 10, 11]


def verhoog_met(lijst, getal):
    resultaat = []
    for i in lijst:
        resultaat.append(i + getal)
    return resultaat


print("de nieuwe lijst is: ", verhoog_met(lijst, 3))
# output = [4, 7, 8, 10, 11, 13, 14]

'''
4. Gebruik de vorige 2 functies om een nieuwe funtie te maken die het laagste getal bij alle getallen in een lijst optelt.
'''
lijst = [1, 4, 5, 7, 8, 10, 11]


def verhoog_met_minimum(lijst):
    minimum_lijst = minimum(lijst)
    resultaat = verhoog_met(lijst, minimum_lijst)
    return resultaat


print("de nieuwe lijst is: ", verhoog_met_minimum(lijst))
# output = [2, 5, 6, 8, 9, 11, 12]
