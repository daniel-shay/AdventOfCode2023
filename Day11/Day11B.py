data = []
emptyR = []
with open("Input/input.txt") as file:
    index = 0
    for line in file:
        data.append([])
        for char in line.strip():
            data[index].append(char)
        if data[len(data) - 1] == ['.']*len(data[len(data) - 1]):
            # data.append(data[len(data) - 1].copy())
            # index += 1
            emptyR.append(len(data) - 1)
        index += 1

cols = len(data[0])
c = 0
emptyC = []
while c < cols:
    empty = True
    for r in range(len(data)):
        if data[r][c] != '.':
            empty = False
    if empty:
        # for r in range(len(data)):
        #     data[r].insert(c, '.')
        # cols += 1
        # c += 1
        emptyC.append(c)
    c += 1

galaxies = []
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] != '.':
            galaxies.append((r, c))

finish = 0
count = 1
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        if galaxies[i] == galaxies[j]:
            continue
        dist = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        for r in emptyR:
            if min(galaxies[i][0], galaxies[j][0]) < r < max(galaxies[i][0], galaxies[j][0]):
                dist += 999999
        for c in emptyC:
            if min(galaxies[i][1], galaxies[j][1]) < c < max(galaxies[i][1], galaxies[j][1]):
                dist += 999999
        finish += dist
        # print(count, galaxies[i], galaxies[j], dist)
        count += 1
print(finish)
