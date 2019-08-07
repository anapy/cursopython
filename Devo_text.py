test1 = 'AB'
def reverse(word):
    result = ''
    long = len(word)
    for char in word:
        char = word[long - 1]
        long = long - 1
        result = result + char
    return result

def compare(new, original):
        if new == original:
            print('Word', original, 'is a palindromo')
        else:
            print('Not a palindromo')

def ispalindrome(word):
    palindrome = True
    lenght = len(word)
    half = int(lenght/2)
    start = 0
    while start < half:
        if word[start] == word[lenght-1]:
            start = start + 1
            lenght = lenght - 1
        else:
            palindrome = False
            break
    return palindrome
#Opción más rápida solo recorre hasta la mitad de la palabra
print(ispalindrome(test1))

#Opción 2 da la vuelta a la palabra, la guarda en una variable y la compara con la original
print(reverse(test1))
result = reverse(test1)
compare(result, test1)
ispalindrome(test1)
