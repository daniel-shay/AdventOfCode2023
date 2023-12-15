import re

with open("Input/input.txt") as file:
    data = file.read()

data = data.replace('\n','')
data = data.split(',')

pattern = re.compile(r'([a-zA-Z]+)([^a-zA-Z]*)')

boxes = dict()
for index in range(256):
    boxes[index] = list()

for string in data:
    instruction = pattern.findall(string)[0]
    label = instruction[0]
    action = instruction[1]
    val = 0
    for char in label:
        val += ord(char)
        val *= 17
        val %= 256

    lenses = boxes.get(val)
    if action == '-':
        for lens in lenses:
            if label in lens:
                lenses.remove(lens)
    else:
        newLens = label + " " + action[1:]
        found = False
        for lensIndex in range(len(lenses)):
            if label in lenses[lensIndex]:
                lenses[lensIndex] = newLens
                found = True
        if not found:
            boxes[val].append(newLens)

total = 0
for boxIndex in range(256):
    lenses = boxes.get(boxIndex)
    for lensIndex in range(len(lenses)):
        lens = lenses[lensIndex]
        focalLength = int(lens.split()[1])
        power = (boxIndex + 1) * (lensIndex + 1) * focalLength
        # print(f'boxIndex:{boxIndex + 1}, lensIndex:{lensIndex + 1}, focalLength:{focalLength}, power:{power}')
        total += power
print(total)
