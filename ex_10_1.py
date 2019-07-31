document = open('mbox-short.txt')
emails = dict()
for line in document:
    if line.startswith('From'):
        line = line.split()
        person = line[1]
        #print(email)
        #person = email.split('@')
        #person = person [0]
        emails [person] = emails.get(person, 0) + 1
print(sorted([(per, time) for time, per in emails.items()], reverse=True))
