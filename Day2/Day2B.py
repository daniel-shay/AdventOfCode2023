powerSum = 0
with open("Inputs/input.txt") as file:
    gameSum = 0
    for line in file:
        red = 0
        green = 0
        blue = 0
        gameNum = int(line[line.find(' '):line.find(':')])
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
                        red = count
                elif cube.find('green') > -1:
                    color = 'green'
                    if count > green:
                        green = count
                elif cube.find('blue') > -1:
                    color = 'blue'
                    if count > blue:
                        blue = count
                else:
                    print("BAD BAD BAD")
                    color = 'bad'
        power = red * green * blue
        powerSum += power
print(powerSum)
