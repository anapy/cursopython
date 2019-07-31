text = open('mbox-short.txt')
result = dict()
order = list()
for line in text:
    lineLower = line.lower()
    #print(line)
    for word in lineLower.split():
        for letter in word:
            if letter >='a' and letter <='z':
                if letter not in result:
                    result[letter] = 1
                else:
                    result[letter] += 1

for value, key in result.items():
    order.append((key, value))
    order.sort(reverse=True)
print(order)
