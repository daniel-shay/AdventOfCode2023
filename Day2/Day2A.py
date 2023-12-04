red = 12
green = 13
blue = 14
with open("Inputs/input.txt") as file:
    gameSum = 0
    for line in file:
        gameNum = int(line[line.find(' '):line.find(':')])
        valid = True
        draws = line[line.find(':')+2:].split(';')
        for draw in draws:
            cubes = draw.split(',')
            for cube in cubes:
                cube = cube.strip(' ')
                count = cube[0:cube.find(' ')]
                count = int(count)
                if cube.find('red') > -1:
                    color = 'red'
                    if count > red:
                        valid = False
                elif cube.find('green') > -1:
                    color = 'green'
                    if count > green:
                        valid = False
                elif cube.find('blue') > -1:
                    color = 'blue'
                    if count > blue:
                        valid = False
                else:
                    print("BAD BAD BAD")
                    color = 'bad'
        if valid:
            print(gameNum)
            gameSum += gameNum
print(gameSum)

