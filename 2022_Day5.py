

data = []
with open('2022_Day5_instructions.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)

print(data)