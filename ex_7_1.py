text = input ('Enter a file name: ')
text = open (text)
for line in text:
    line = line.rstrip ()
    line = line.upper ()
    print (line)
