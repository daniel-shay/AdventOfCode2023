winnings = dict()
for i in range(1, 209):
    winnings[i] = 1

with open("Input/input.txt") as file:
    card = 0
    for line in file:
        card += 1
        line = line[line.find(":")+2:]
        sets = line.split("|")
        winners = sets[0].split()
        mine = sets[1].split()
        count = 0

        for num in mine:
            if num in winners:
                # print(num)
                count += 1

        for j in range(0, winnings[card]):
            for i in range(card+1, card+1+count):
                winnings[i] = winnings[i] + 1

sum = 0
for i in winnings.values():
    sum += i
print(sum)
