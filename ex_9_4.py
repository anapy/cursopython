email = open('mbox-short.txt')
emailaddress = dict()
mostcount = 0
mostpopullar = None
for line in email:
    if line.startswith('From'):
        line = line.split()
        if len(line) >= 3:
            emailaddress [line[1]] = emailaddress.get(line[1], 0) + 1
            for popullar, count in emailaddress.items():
                if mostcount < count:
                    mostpopullar = popullar
                    mostcount = count
print(mostpopullar, mostcount)
