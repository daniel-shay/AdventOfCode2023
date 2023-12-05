def check_range(item, source, destination, range):

    if source <= item < source + range:
        return destination + item - source
    else:
        return item


def get_value(input, ranges):
    rtrn = 0
    for data in ranges:
        elements = data.split()
        possible = check_range(int(input), int(elements[1]), int(elements[0]), int(elements[2]))
        if possible != int(input):
            rtrn = possible
    if rtrn == 0:
        rtrn = int(input)

    return rtrn


class SeedInfo:
    def __init__(self, seed, soil, fertilizer, water, light, temperature, humidity, location):
        self.seed = seed
        self.soil = soil
        self.fertilizer = fertilizer
        self.water = water
        self.light = light
        self.temperature = temperature
        self.humidity = humidity
        self.location = location

    def print(self):
        print("Seed:" + str(self.seed))
        print("soil:" + str(self.soil))
        print("fertilizer:" + str(self.fertilizer))
        print("water:" + str(self.water))
        print("light:" + str(self.light))
        print("temperature:" + str(self.temperature))
        print("humidity:" + str(self.humidity))
        print("location:" + str(self.location))


seeds2Soil = []
soil2Fertilizer = []
fertilizer2Water = []
water2Light = []
light2Temperature = []
temperature2Humidity = []
humidity2Location = []
with open("Input/input.txt") as file:
    item = -1
    for line in file:
        if line == '\n':
            continue
        if item == -1:
            seeds = line
            item = 0

        if line == 'seed-to-soil map:\n':
            item = 1
            continue
        elif line == 'soil-to-fertilizer map:\n':
            item = 2
            continue
        elif line == 'fertilizer-to-water map:\n':
            item = 3
            continue
        elif line == 'water-to-light map:\n':
            item = 4
            continue
        elif line == 'light-to-temperature map:\n':
            item = 5
            continue
        elif line == 'temperature-to-humidity map:\n':
            item = 6
            continue
        elif line == 'humidity-to-location map:\n':
            item = 7
            continue
        # else:
        #     print(";" + line + "'")

        if item == 1:
            seeds2Soil.append(line)
        elif item == 2:
            soil2Fertilizer.append(line)
        elif item == 3:
            fertilizer2Water.append(line)
        elif item == 4:
            water2Light.append(line)
        elif item == 5:
            light2Temperature.append(line)
        elif item == 6:
            temperature2Humidity.append(line)
        elif item == 7:
            humidity2Location.append(line)

seeds = seeds.split()[1:]

seedInfos = []

for i in range(int(len(seeds)/2)):
    # print(i)
    for j in range(int(seeds[i * 2 + 1])):
        # print(j)
        seed = int(seeds[i * 2]) + j
        soil = get_value(seed, seeds2Soil)
        fertilizer = get_value(soil, soil2Fertilizer)
        water = get_value(fertilizer, fertilizer2Water)
        light = get_value(water, water2Light)
        temperature = get_value(light, light2Temperature)
        humidity = get_value(temperature, temperature2Humidity)
        location = get_value(humidity, humidity2Location)

        seedInfos.append(SeedInfo(seed, soil, fertilizer, water, light, temperature, humidity, location))

curMin = 1015522767999
for seedInfo in seedInfos:
    # seedInfo.print()
    # print()
    if seedInfo.location < curMin:
        curMin = seedInfo.location

# seedInfos[26].print()
print(curMin)
