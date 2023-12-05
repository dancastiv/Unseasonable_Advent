
def addition(data):
    digits = ''
    numbers = []
    for i in data:
        if i.isalpha():
            pass
        else:
            for letter in i:
                if letter.isnumeric():
                    digits += letter
            numbers.append(digits[0] + digits[-1])
            digits = ''
        numbers = list(map(int, numbers))
        return sum(numbers)
    
def addition_reloaded(data):
    digits = ''
    numbers = []
    for i in data:
        if 'two' in i:
            i = i.replace('two', '2')
            print('bitch')
    print(data)
    for i in data:
        for letter in i:
            if letter.isnumeric():
                digits += letter
        numbers.append(digits[0] + digits[-1])
        digits = ''
    numbers = list(map(int, numbers))
    return sum(numbers)


data = []
with open('2023_Day1_calibration.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)

sum = addition(data)
sum_reloaded = addition_reloaded(data)




print(sum)
print(sum_reloaded)

"""
if 'one' in i:
            i = i.replace('one', '1')
        elif 'two' in i:
            i = i.replace('two', '2')
            print('mewo')
        i = i.replace('three', '3')
        i = i.replace('four', '4')
        i = i.replace('five', '5')
        i = i.replace('six', '6')
        i = i.replace('seven', '7')
        i = i.replace('eight', '8')
        i = i.replace('nine', '9')
        """