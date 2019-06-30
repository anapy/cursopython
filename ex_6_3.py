
word = input('Introduce word: ')
letter = input('Introduce letter: ')

#esta función cuenta el número de letras que aparece en una palabra
def count(word, letter):
    cuenta = 0
    for char in word:
        if char == letter:
            cuenta = cuenta + 1
    return cuenta
print(count(word, letter))
