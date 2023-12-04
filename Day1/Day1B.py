import re

def stringToInt(firstS):
    if firstS == 'one':
        first = 1
    elif firstS == 'two':
        first = 2
    elif firstS == 'three':
        first = 3
    elif firstS == 'four':
        first = 4
    elif firstS == 'five':
        first = 5
    elif firstS == 'six':
        first = 6
    elif firstS == 'seven':
        first = 7
    elif firstS == 'eight':
        first = 8
    elif firstS == 'nine':
        first = 9
    else:
        first = int(firstS)
    return first


total = 0
with open("Day1AInput.txt") as inputFile:
    for line in inputFile:
        nums = re.findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', line)
        first = stringToInt(nums[0])
        numsReversed = re.findall(r'[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', str(line[::-1]))
        second = stringToInt(str(numsReversed[0][::-1]))
        current = int(str(first) + str(second))
        total += current
        # print("total: " + str(total))
print(total)
