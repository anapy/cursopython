import re
tryee = open('mbox-short.txt')
count = 0
reexp = input('Enter a regular expression: ')
for line in tryee:
    line = line.rstrip()
    result = re.findall(reexp, line)
    if len(result) > 0:
        count = count + 1
print(count)
