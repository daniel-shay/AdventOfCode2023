with open("Input/input.txt") as file:
    data = file.read()

data = data.replace('\n','')
data = data.split(',')

sum = 0
for string in data:
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    sum += val
    print(val)
print(sum)
