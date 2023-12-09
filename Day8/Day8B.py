import math
import re
from functools import reduce

with open("Input/input.txt") as file:
    data = file.read().split('\n')

directions = data[0]

coors = dict()
current = []
for index in range(2,len(data)):
    cur = re.split(r"\W+", data[index])
    start = cur[0]
    coors[start] = (cur[1], cur[2])
    if start[-1] == 'A':
        current.append(start)

count = 0
counts = [0]*len(current)
index = 0
while True:
    if count % 10000000 == 0:
        print("current: ", current)
        print("counts: ", counts)
        print("count: ", count)

    if index == len(directions):
        index = 0

    for i in range(len(current)):
        if current[i][-1] == 'Z' and counts[i] == 0:
            counts[i] = count

    done = True
    for item in counts:
        if item == 0:
            done = False
    if done:
        break

    dir = 0 if directions[index] == 'L' else 1
    for i in range(len(current)):
        current[i] = coors[current[i]][dir]
    index += 1
    count += 1

print("final: ", counts)
print(reduce((lambda x, y: abs(x*y) // math.gcd(x, y)), counts))
