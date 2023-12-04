with open("Input/input.txt") as file:
    final = 0
    for line in file:
        line = line[line.find(":")+2:]
        sets = line.split("|")
        winners = sets[0].split()
        mine = sets[1].split()
        score = 0.5

        for num in mine:
            if num in winners:
                # print(num)
                score *= 2

        if score == 0.5:
            score = 0
        final += score
        # print(str(score))
print(final)