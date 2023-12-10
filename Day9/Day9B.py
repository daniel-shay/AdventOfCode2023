with (open("Input/input.txt") as file):
    counter = 0
    for line in file:
        sequences = [list(map(int, line.split()))]
        for i in range(100):
            if sequences[i] == [0] * len(sequences[i]):
                break
            sequences.append([])
            for j in range(len(sequences[i])-1):
                sequences[i+1].append(sequences[i][j+1] - sequences[i][j])

        sequences[-1].append(0)
        for i in range(len(sequences)-1, 0, -1):
            sequences[i-1].insert(0, sequences[i-1][0] - sequences[i][0])
        counter += sequences[0][0]
        print(sequences)
    print(counter)
