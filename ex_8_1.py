ex = ['Ana', 'María', 'Pepa', 'Josefa', 'Marta']
pepito = ['Ana', 'María', 'Pepa']
def chop(lista):
    del lista[0]
    del lista[len(lista)-1]

def middle(lista):
    return lista[1:len(lista)-1]

#ex = input('Introduce your list: ')
#ex = ex.split(',')
print(chop(pepito))
#print(middle(pepito))
print(pepito)
