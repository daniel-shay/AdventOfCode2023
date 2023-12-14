data = []
with open("Input/input.txt") as file:
    for line in file:
        data.append([])
        for char in line.strip():
            data[len(data) - 1].append(char)

for cycle in range(1, 10001):
    # North
    for c in range(len(data[0])):
        # print(f'c:{c}')
        spot = 0
        for r in range(len(data)):
            # print(f'r:{r}')
            char = data[r][c]
            if char == 'O':
                data[r][c] = '.'
                data[spot][c] = 'O'
                # print(f'r:{r}, c:{c}, spot:{spot}')
                spot += 1
            if char == '#':
                spot = r + 1

    # West
    for r in range(len(data)):
        spot = 0
        for c in range(len(data[0])):
            char = data[r][c]
            if char == 'O':
                data[r][c] = '.'
                data[r][spot] = 'O'
                # print(f'r:{r}, c:{c}, spot:{spot}')
                spot += 1
            if char == '#':
                spot = c + 1

    # South
    for c in range(len(data[0]) - 1, -1, -1):
        # print(f'c:{c}')
        spot = len(data) - 1
        for r in range(len(data) - 1, -1, -1):
            # print(f'r:{r}')
            char = data[r][c]
            if char == 'O':
                data[r][c] = '.'
                data[spot][c] = 'O'
                # print(f'r:{r}, c:{c}, spot:{spot}')
                spot -= 1
            if char == '#':
                spot = r - 1

    # East
    for r in range(len(data) - 1, -1, -1):
        spot = len(data[0]) - 1
        for c in range(len(data[0]) - 1, -1, -1):
            char = data[r][c]
            if char == 'O':
                data[r][c] = '.'
                data[r][spot] = 'O'
                # print(f'r:{r}, c:{c}, spot:{spot}')
                spot -= 1
            if char == '#':
                spot = c - 1

    if cycle % 100 == 0:
        total = 0
        for r in range(len(data)):
            load = len(data) - r
            # print(f'r:{r}, load:{load}')
            for char in data[r]:
                # print(char, end='')
                if char == 'O':
                    total += load
            # print()
        print(f'cycle:{cycle} total:{total}')
