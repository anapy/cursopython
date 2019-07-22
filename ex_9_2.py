email = open('mbox-short.txt')
emailsday = dict()
for line in email:
    if line.startswith('From'):
        line = line.split()
        if len(line) >= 3:
            #print(line[2])
            emailsday [line[2]] = emailsday.get(line[2], 0) + 1
print(emailsday)
