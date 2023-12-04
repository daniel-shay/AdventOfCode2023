
def checkForSymbols(data, r, c):
    try:
        cell = data[r - 1][c - 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r - 1][c]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r - 1][c + 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r][c - 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r][c + 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r + 1][c - 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r + 1][c]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    try:
        cell = data[r + 1][c + 1]
        try:
            digit = int(cell)
        except ValueError:
            if cell != '.':
                return True
    except IndexError:
        pass

    return False

sum = 0
data = []
with open("Inputs/input.txt") as file:
    for line in file:
        data.append(line.strip('\n'))
continuing = False
currentNumber = 0
isPart = False
for r in range(len(data)):
    for c in range(len(data[r])):
        char = data[r][c]
        if c == 0:
            if isPart and continuing:
                sum += currentNumber
                print("isPart: " + str(currentNumber))
            elif not isPart and continuing:
                print("notPart: " + str(currentNumber))
                pass
            continuing = False
            isPart = False

        try:
            digit = int(char)
            isDigit = True
            if not isPart:
                isPart = checkForSymbols(data, r, c)
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
            if isPart:
                sum += currentNumber
                print("isPart: " + str(currentNumber))
            else:
                print("notPart: " + str(currentNumber))
                pass
            isPart = False

print(sum)
