from functools import cmp_to_key

ordering = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# ordering.index('J')

# High Card = 1
# One Pair = 2
# Two Pair = 3
# Three of a Kind = 4
# Full House = 5
# Four of a Kind = 6
# Five of a Kind = 7

def countPairs(counts):
    pairs = 0
    for count in counts:
        if count == 2:
            pairs += 1
    return pairs

def get_type(a):
    cardCount = dict()
    cards = a[0]

    for card in cards:
        previous = cardCount.get(card)
        if previous is None:
            cardCount[card] = 1
        else:
            cardCount[card] = previous + 1

    counts = cardCount.values()
    if 5 in counts:
        return 7
    elif 4 in counts:
        return 6
    elif 3 in counts and 2 in counts:
        return 5
    elif 3 in counts:
        return 4
    elif countPairs(counts) == 2:
        return 3
    elif countPairs(counts) == 1:
        return 2
    else:
        return 1


def compCards(a, b):
    for i in range(5):
        if ordering.index(a[i]) == ordering.index(b[i]):
            pass
        elif ordering.index(a[i]) > ordering.index(b[i]):
            return 1
        else:
            return -1
    return 0

def comp(a, b):
    aType = get_type(a)
    bType = get_type(b)

    if aType == bType:
        return compCards(a[0], b[0])
    elif aType > bType:
        return 1
    else:
        return -1


data = list()
with open("Input/input.txt") as file:
    for line in file:
        line = line.split()
        data.append((line[0], line[1]))

# for hand in data:
#     print(get_type(hand))

data = sorted(data, key=cmp_to_key(comp))

winnings = 0
for i in range(len(data)):
    print(data[i])
    winnings += int(data[i][1]) * (i + 1)

print(winnings)
