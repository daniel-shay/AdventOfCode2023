import math
import re


def build_pattern(in_pattern: str):
    nums = in_pattern.split(',')
    begin = r'\.*'
    end = r'\.*'
    mid = r''
    mid += '#{' + nums[0] + '}'

    for index in range(1, len(nums) - 1):
        mid += r'\.+#{' + nums[index] + '}'

    if len(nums) > 1:
        mid += r'\.+#{' + nums[len(nums) - 1] + '}'

    return begin + mid + end


def place_spring(springs: str, pattern: str):
    # print(f'springs: %s, pattern: %s, count: %s' % (springs, pattern, count))
    if '?' in springs:
        count1 = place_spring(springs.replace('?', '#'), pattern)
        # print(f'count1: %s' % count)
        count2 = place_spring(springs.replace('?', '.'), pattern)
        # print(f'count2: %s' % count)
        return count1 + count2
    elif re.fullmatch(pattern, springs):
        # print(f'springs: {springs}, pattern: {pattern}, count: {count}')
        return 1
    else:
        return 0


with open("Input/example.txt") as file:
    final = 0
    for line in file:
        # line = file.readline()
        line = line.split()
        springs = line[0]  # ((line[0] + '?') * 2)[:-1]
        pattern = line[1]  # ((line[1] + ',') * 2)[:-1]

        pattern = build_pattern(pattern.strip())
        # print(pattern)
        count = place_spring(springs, pattern)

        springs = ((line[0] + '?') * 2)[:-1]
        pattern = ((line[1] + ',') * 2)[:-1]
        print(f'springs: {springs}, pattern: {pattern}')
        count2 = place_spring(springs, pattern)

        print(f"count: {count}, count2: {count2}")
        print(f"count^4: {math.pow(count2/count, 3)}")
        final += count
    print(final)
