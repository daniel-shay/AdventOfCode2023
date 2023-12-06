with open("Input/inputB.txt") as file:
    times = file.readline()
    distances = file.readline()

times = times.split()
distances = distances.split()

overall = 1
for i in range(1, len(times)):
    count = 0
    for j in range(1,int(times[i])):
        dist = j * (int(times[i]) - j)
        # print(int(distances[i]))
        if dist > int(distances[i]):
            count += 1
    print(count)
    overall *= count
print(overall)
# print(times)
# print(distances)
