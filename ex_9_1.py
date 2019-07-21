wordsdict = dict()
file = open('words.txt')
for line in file:
    words = line.split( )
    for word in words:
        wordsdict[word] = 1
print(wordsdict)
print('will' in wordsdict)
