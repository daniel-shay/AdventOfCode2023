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
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] == 'S':
            current = (r, c)

# print(current)

# find next
target = (-1, -1)
compass = ''
if get_char(data, apply_offset(current, (0, 1))) in pipes:
    target = apply_offset(current, (0, 1))
    compass = 'right'
elif get_char(data, apply_offset(current, (-1, 0))) in pipes:
    target = apply_offset(current, (-1, 0))
    compass = 'up'
elif get_char(data, apply_offset(current, (1, 0))) in pipes:
    target = apply_offset(current, (1, 0))
    compass = 'down'
elif get_char(data, apply_offset(current, (0, -1))) in pipes:
    target = apply_offset(current, (0, -1))
    compass = 'left'


# print(target)

# traverse
count = 1
for i in range(145*145):
    target2 = (-1, -1)
    tar = get_char(data, target)
    print(target)
    print(compass)
    print(tar)
    if tar == '|':  # is a vertical pipe connecting north and south.
        target2 = (target[0] + (-1 if compass == 'up' else 1), target[1])
    elif tar == '-':  # is a horizontal pipe connecting east and west.
        target2 = (target[0], target[1] + (1 if compass == 'right' else -1))
    elif tar == 'L':  # is a 90-degree bend connecting north and east.
        if compass == 'down':
            target2 = (target[0], target[1] + 1)
            compass = 'right'
        else:
            target2 = (target[0] - 1, target[1])
            compass = 'up'
    elif tar == 'J':  # is a 90-degree bend connecting north and west.
        if compass == 'down':
            target2 = (target[0], target[1] - 1)
            compass = 'left'
        else:
            target2 = (target[0] - 1, target[1])
            compass = 'up'
    elif tar == '7':  # is a 90-degree bend connecting south and west.
        if compass == 'right':
            target2 = (target[0] + 1, target[1])
            compass = 'down'
        else:
            target2 = (target[0], target[1] - 1)
            compass = 'left'
    elif tar == 'F':  # is a 90-degree bend connecting south and east.
        if compass == 'up':
            target2 = (target[0], target[1] + 1)
            compass = 'right'
        else:
            target2 = (target[0] + 1, target[1])
            compass = 'down'
    elif tar == 'S':  # is the starting position of the animal
        break

    count += 1
    current = target
    target = target2
print(count)
print(count // 2)
