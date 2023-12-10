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

        for i in range(len(sequences)-1, 0, -1):
            sequences[i-1].append(sequences[i][-1] + sequences[i-1][-1])
        counter += sequences[0][-1]
        print(sequences)
    print(counter)