'''
1. Maak een functie die alle cijfers in een lijst optelt
'''

lijst = [1, 4, 5, 7, 8, 10, 11]
print("de som is: ", som(lijst))
# ouput = 46

'''
2. Maak een functie die het laagste getal in een lijst bapaalt.
'''
lijst = [1, 4, 5, 7, 8, 10, 11]
print("het laagste getal is: ", minimum(lijst))
# ouput = 1

'''
3. Maak een functie die een getal bij elk getal in een lijst optelt.
'''

lijst = [1, 4, 5, 7, 8, 10, 11]

print("de nieuwe lijst is: ", verhoog_met(lijst, 3))
# output = [4, 7, 8, 10, 11, 13, 14]

'''
4. Gebruik de vorige 2 functies om een nieuwe funtie te maken die het laagste getal bij alle getallen in een lijst optelt.
'''
lijst = [1, 4, 5, 7, 8, 10, 11]

print("de nieuwe lijst is: ", verhoog_met_minimum(lijst))
# output = [2, 5, 6, 8, 9, 11, 12]
