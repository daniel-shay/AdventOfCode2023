
def checkForGears(data, r, c):
    gears = set()
    try:
        cell = data[r - 1][c - 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r - 1, c -1))
    except IndexError:
        pass

    try:
        cell = data[r - 1][c]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r -1, c))
    except IndexError:
        pass

    try:
        cell = data[r - 1][c + 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r - 1, c + 1))
    except IndexError:
        pass

    try:
        cell = data[r][c - 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r, c - 1))
    except IndexError:
        pass

    try:
        cell = data[r][c + 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r, c + 1))
    except IndexError:
        pass

    try:
        cell = data[r + 1][c - 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r + 1, c - 1))
    except IndexError:
        pass

    try:
        cell = data[r + 1][c]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r + 1, c))
    except IndexError:
        pass

    try:
        cell = data[r + 1][c + 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell == '*':
                gears.add((r + 1, c + 1))
    except IndexError:
        pass

    return gears

data = []
with open("Inputs/input.txt") as file:
    for line in file:
        data.append(line.strip('\n'))
continuing = False
currentNumber = 0
gears = set()
final = dict()

for r in range(len(data)):
    for c in range(len(data[r])):
        char = data[r][c]
        if c == 0:
            if continuing:
                # print(str(currentNumber) + " " + str(gears))
                for gear in gears:
                    previous = final.get(gear)
                    if previous is not None:
                        # print(previous)
                        final[gear] = {currentNumber}.union(previous)
                    else:
                        final[gear] = {currentNumber}
                    # print(final[gear])
                gears = set()
            continuing = False

        try:
            digit = int(char)
            isDigit = True
            gears = gears.union(checkForGears(data, r, c))
        except ValueError:
            isDigit = False

        if not continuing and isDigit:
            currentNumber = int(char)
            continuing = True
        elif isDigit:
            currentNumber = int(str(currentNumber) + char)
        elif not continuing and not isDigit:
            pass
        else:
            continuing = False
            # print(str(currentNumber) + " " + str(gears))
            for gear in gears:
                previous = final.get(gear)
                if previous is not None:
                    # print(previous)
                    final[gear] = {currentNumber}.union(previous)
                else:
                    final[gear] = {currentNumber}
                # print(final[gear])
            gears = set()

answer = 0
for gear in final.keys():
    parts = final[gear]
    if len(parts) == 2:
        print(parts)
        ratio = 1
        for part in parts:
            ratio *= part
        print(ratio)
        answer += ratio
print(answer)