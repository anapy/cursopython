#fname = input('Enter a file name: ')
text = open('mbox-short.txt')
count = 0
for line in text:
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1])
        continue
print("There were", count, "lines in the file with From as the first word")
