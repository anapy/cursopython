document = open('mbox-short.txt')
hours= dict()
for line in document:
    if line.startswith('From'):
        line = line.split()
        if len(line) >= 4:
            hour = line[5]
            hour = hour.split(':')
            hour = hour[0]
            hours [hour] = hours.get(hour, 0) + 1
count = list()
for ho, times in hours.items():
    count.append((ho, times))
count.sort()
for times, ho in count:
    print(times, ho)
#print(count)
#print(sorted([(ho, time) for time, ho in hours.items()], reverse=True))
