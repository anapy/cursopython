import re
text = open('regex_ex.txt')
sum = 0
for line in text:
    numbers = re.findall('([0-9]+)', line)
    for number in numbers:
        number = int(number)
        sum = sum + number
print(sum)
    #if len(numbers) > 0:
        #print(numbers)
