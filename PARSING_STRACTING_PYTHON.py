data = 'saludad a Hope!'
x = data.find('l')
print(x)
y = data.find('H', x)
print(y)
z = data[x : y]
print(z)
