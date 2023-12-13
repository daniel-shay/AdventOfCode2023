# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

pipes = '|-LJ7F'


def get_char(data, coor):
    try:
        return data[coor[0]][coor[1]]
    except IndexError:
        return ''


def apply_offset(coor, offset):
    return coor[0] + offset[0], coor[1] + offset[1]


data = []
with open("Input/input.txt") as file:
    index = 0
    for line in file:
        data.append([])
        for char in line.strip():
            data[index].append(char)
        index += 1

# find start
current = (-1, -1)
output = []
for r in range(len(data)):
    output.append([])
    for c in range(len(data[r])):
        output[r].append(' ')
        if data[r][c] == 'S':
            current = (r, c)
        elif data[r][c] == '.':
            output[r][c] = '.'

# print(current)

# find next
target = (-1, -1)
compass = ''
u_d = ''
if get_char(data, apply_offset(current, (0, 1))) in pipes:
    target = apply_offset(current, (0, 1))
    compass = 'r'
elif get_char(data, apply_offset(current, (-1, 0))) in pipes:
    target = apply_offset(current, (-1, 0))
    compass = 'u'
    u_d = 'u'
elif get_char(data, apply_offset(current, (1, 0))) in pipes:
    target = apply_offset(current, (1, 0))
    compass = 'd'
    u_d = 'd'
elif get_char(data, apply_offset(current, (0, -1))) in pipes:
    target = apply_offset(current, (0, -1))
    compass = 'l'


# print(target)

# traverse
count = 1
for i in range(145*145):
    target2 = (-1, -1)
    tar = get_char(data, target)
    # print(target)
    # print(compass)
    # print(tar)
    if tar == '|':  # is a vertical pipe connecting north and south.
        target2 = (target[0] + (-1 if compass == 'u' else 1), target[1])
    elif tar == '-':  # is a horizontal pipe connecting east and west.
        target2 = (target[0], target[1] + (1 if compass == 'r' else -1))
    elif tar == 'L':  # is a 90-degree bend connecting north and east.
        if compass == 'd':
            target2 = (target[0], target[1] + 1)
            compass = 'r'
        else:
            target2 = (target[0] - 1, target[1])
            compass = 'u'
            u_d = 'u'
    elif tar == 'J':  # is a 90-degree bend connecting north and west.
        if compass == 'd':
            target2 = (target[0], target[1] - 1)
            compass = 'l'
        else:
            target2 = (target[0] - 1, target[1])
            compass = 'u'
            u_d = 'u'
    elif tar == '7':  # is a 90-degree bend connecting south and west.
        if compass == 'r':
            target2 = (target[0] + 1, target[1])
            compass = 'd'
            u_d = 'd'
        else:
            target2 = (target[0], target[1] - 1)
            compass = 'l'
    elif tar == 'F':  # is a 90-degree bend connecting south and east.
        if compass == 'u':
            target2 = (target[0], target[1] + 1)
            compass = 'r'
        else:
            target2 = (target[0] + 1, target[1])
            compass = 'd'
            u_d = 'd'
    elif tar == 'S':  # is the starting position of the animal
        break
    output[target[0]][target[1]] = u_d

    count += 1

    # print(current)

    current = target
    target = target2
# print(count)
# print(count // 2)

point = 0
for r in range(len(output)):
    count = 0
    countU = 0
    countL = 0
    countR = 0
    countD = 0
    tail = ''
    for c in range(len(output[r])):
        char = output[r][c]
        print(char, end='')
        found = False
        if char == '.':
            for c2 in range(c - 1, -1, -1):
                if output[r][c2] == 'u':
                    point += 1
                    found = True
                elif output[r][c2] == 'd':
                    break
            if not found:
                for c2 in range(c + 1, len(output[r])):
                    if output[r][c2] == 'd':
                        point += 1
                        found = True
                        print(c2, end='')
                    elif output[r][c2] == 'u':
                        break
    #     if char == 'u':
    #         count = 1
    #         countU += 1
    #     elif char == 'r':
    #         count = 1
    #         countR += 1
    #     elif char == 'd':
    #         count = -1
    #         countD += 1
    #     elif char == 'l':
    #         # count = -1
    #         countL += 1
    #     elif char == '.':
    #         if count > 0:
    #             point += 1
    #         tail += str.join(', ', [str(count), str(countU), str(countR), str(countD), str(countL), '+'])
    # print("count: " + str(count) + ", point: " + str(point) + '    ' + tail)
    print("count: " + str(count) + ", point: " + str(point))
print(point)
