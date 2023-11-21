
depths = []
with open('2021_Day1_depths.txt') as file:
    for line in file:
        line = line.strip()
        depths.append(line)
counter = 0        
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        counter += 1

print(f"The total number of depths increases is: {counter}.")