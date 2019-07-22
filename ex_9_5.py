email = open('mbox-short.txt')
domain = dict()
for line in email:
    if line.startswith('From'):
        line = line.split()
        if len(line) >= 3:
            emailaddress = line[1].split('@')
            at = emailaddress[1]
            domain [at] = domain.get(at, 0) + 1
print(domain)
