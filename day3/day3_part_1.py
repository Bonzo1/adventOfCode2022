import math

smallLetters = 'abcdefghijklmnopqrstuvwxyz'
capitalLetters = smallLetters.upper()
allItems = []
with open("input_1.txt", 'r') as file:
    for rucksack in file.read().splitlines():
        x = int((len(rucksack)/2))
        firstCompartment, secondCompartment = rucksack[:x], rucksack[x:]
        allItems.append((firstCompartment, secondCompartment))

totalPriorities = []
for rucksack in allItems:
    foundChar = False
    commonchar = ''
    firstCompartment = rucksack[0]
    secondCompartment = rucksack[1]
    for char in firstCompartment:
        for char2 in secondCompartment:
            if (char == char2):
                commonchar = char
                _prio = smallLetters.find(commonchar)
                priority = _prio+1
                if _prio < 0:
                    priority = capitalLetters.find(commonchar)+27
                totalPriorities.append(int(priority))
                foundChar = True
            if foundChar:
                break
        if foundChar:
            break
print(f'Total priority: {math.fsum(totalPriorities)}')