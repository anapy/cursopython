#función: busca las líneas en cualquier texto, las analiza sin repetidas y las ordena alfabéticamente
def email_day(filename):
    #fname = input("Enter file name: ")
    file = open(filename)
    lst = list()
    for line in file:
        line = line.rstrip()
        wordlist = line.split()
        for word in wordlist:
           if word in lst: continue
           else: lst.append(word)
    lst.sort()
    return lst

print(email_day('romeo.txt'))
