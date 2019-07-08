a = list()
while True:
    number = input('Enter a number: ')
    if number != 'done':
        a.append(number)
        #print(a)
    else:
        break
print('Maximum: ', float(max(a)))
print('Minimum: ', float(min(a)))
