import re

with open("Inputs/input.txt") as file:
    data = file.read()
    splits = re.split(r'[0-9]|\.+', data)
    set = set()
    for i in splits:
        set.add(i)
    print(set)
