import math

smallLetters = 'abcdefghijklmnopqrstuvwxyz'
capitalLetters = smallLetters.upper()
allItems = []
split = 0
elfGroup = []
with open("input_1.txt", 'r') as file:
    for rucksack in file.read().splitlines():
        split+=1
        elfGroup.append(rucksack)
        if split % 3 == 0 and split > 0:
            allItems.append(elfGroup)
            elfGroup = []
        

totalPriorities = []
for rucksack in allItems:
    foundChar = False
    commonchar = ''
    firstRucksack = rucksack[0]
    secondRucksack = rucksack[1]
    thirdRucksack = rucksack[2]
    for char in firstRucksack:
        for char2 in secondRucksack:
            for char3 in thirdRucksack:
                if (char == char2 == char3):
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
        if foundChar:
            break
print(f'Total priority: {math.fsum(totalPriorities)}')