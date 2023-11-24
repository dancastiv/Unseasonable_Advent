def find_redundancy(pairs):
    first = []
    second = []
    counter = 0
    for i in pairs:
        first = list(map(int, i[0].split("-")))
        second = list(map(int, i[1].split("-")))
        if (first[0] <= second[0]) and (first[1] >= second[1]):
            counter += 1
        elif (first[0] >= second[0]) and (first[1] <= second[1]):
            counter += 1
    return counter

data = []
pairs = []
with open('2022_Day4_pairs.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)
for i in data:
   pairs.append(i.split(","))

counter = find_redundancy(pairs)


print(counter)
