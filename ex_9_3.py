email = open('mbox-short.txt')
emailaddress = dict()
for line in email:
    if line.startswith('From'):
        line = line.split()
        if len(line) >= 3:
            emailaddress [line[1]] = emailaddress.get(line[1], 0) + 1
print(emailaddress)
