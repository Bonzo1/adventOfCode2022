import math

input = []
elfs = []
singleElf = []
with open("input_1.txt", 'r') as file:
    for elfCalorie in file.read().splitlines():
        if (elfCalorie == ''):
            elfs.append(singleElf)
            singleElf = []
            continue
        singleElf.append(elfCalorie)

allElfCalories = []
for elf in elfs:
    elfCalorie = 0
    for calories in elf:
        elfCalorie+=int(calories)
    allElfCalories.append(int(elfCalorie))
allElfCalories.sort()
print(f'Total calories: {math.fsum(allElfCalories[-3:])}')