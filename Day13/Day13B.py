def check_reflection(data_set):
    mirror_r = -1
    for r in range(1, len(data_set)):
        # if True:
        #     r = 4
        #     print(r)
        match = True
        found_smudge = False
        for r2 in range(r - 1, -1, -1):
            try:
                # print(f"1: {dataSet[r2]}, 2: {dataSet[r * 2 - r2 - 1]}, r2: {r2}, r: {r * 2 - r2 - 1}")
                line1 = data_set[r * 2 - r2 - 1]
                line2 = data_set[r2]
                if line1 != line2:
                    if found_smudge:
                        match = False
                        found_smudge = False
                        break
                    else:
                        diff_count = 0
                        for char1, char2 in zip(line1, line2):
                            if char1 != char2:
                                diff_count += 1
                                if diff_count > 1:
                                    match = False
                                    break
                                else:
                                    found_smudge = True
            except IndexError:
                pass
        if match and found_smudge:
            mirror_r = r - 1
            break
    return mirror_r


dataSets = [[]]
with open("Input/input.txt") as file:
    for line in file:
        line = line.strip()
        if line == '':
            dataSets.append([])
        else:
            dataSets[-1].append(line)

final = 0
for dataSet in dataSets:
    mirrorR = check_reflection(dataSet)
    # if mirrorR > 0:
    #     print(f'mirrorR = {mirrorR}, line = {dataSet[mirrorR]}')

    dataSetC = list(zip(*reversed(dataSet)))
    dataSetC = [list(element) for element in dataSetC]

    mirrorC = check_reflection(dataSetC)
    # if mirrorC > 0:
    #     print(f'mirrorC = {mirrorC}, line = {dataSetC[mirrorC]}')
    if mirrorR < 0 and mirrorC < 0:
        print(dataSet)
        break
    elif mirrorR > -1:
        score = 100 * (mirrorR + 1)
        print(f'scoreR: {score}')
        for line in dataSet:
            print(line)
        print()
    else:
        score = mirrorC + 1
        print(f'scoreC: {score}')
        for line in dataSetC:
            print(''.join(line))
        print()
    final += score
print(final)
