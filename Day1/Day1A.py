import re
total = 0
with open("Day1AInput.txt") as inputFile:
    for line in inputFile:
        numsA = re.split(r'[^1-9]+', line)
        for element in numsA:
            if element != '':
                first = element[0]
                break
        for element in reversed(numsA):
            if element != '':
                second = element[-1]
                break
        total += int(first+second)
print(total)