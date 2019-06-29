fname = input("Enter file name: ")
fname = open(fname)
count = 0
result = 0
for line in fname:
    if line.startswith ('X-DSPAM-Confidence: '):
        count = count + 1
        number = line [20:26]
        number = float(number)
        result = result + number
print(count)
print(result)
average = result/count
print('Average spam confidence: ', average)
