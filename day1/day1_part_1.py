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

mostCalories = 0
for elf in elfs:
    elfCalorie = 0
    for calories in elf:
        elfCalorie+=int(calories)
    if elfCalorie > mostCalories:
        mostCalories = elfCalorie
print(mostCalories)