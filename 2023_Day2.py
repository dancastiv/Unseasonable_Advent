

data = []
with open('2023_Day2_games.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)

print(data)