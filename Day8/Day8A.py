import re

with open("Input/input.txt") as file:
    data = file.read().split('\n')

directions = data[0]

coors = dict()
for index in range(2,len(data)):
    cur = re.split(r"\W+", data[index])
    coors[cur[0]] = (cur[1], cur[2])

count = 0
current = 'AAA'
index = 0
for i in range(10000000):
    print(current)
    if index == len(directions):
        index = 0
    if current == 'ZZZ':
        break

    dir = 0 if directions[index] == 'L' else 1
    current = coors[current][dir]
    index += 1
    count += 1

print(count)
