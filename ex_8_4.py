fname = input("Enter file name: ")
file = open(fname)
lst = list()
#print(lst)
for line in file:
    line = line.rstrip()
    wordlist = line.split()
    for word in wordlist:
        if word in lst: continue
            #print(word)
        else:
            lst.append(word)
            #roprint(lst)
lst.sort()
print(lst)
