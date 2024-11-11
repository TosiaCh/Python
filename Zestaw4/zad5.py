"""
ZADANIE 5 - Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru 
left do right włącznie. Lista jest modyfikowana w miejscu (in place). 
Rozważyć wersję iteracyjną i rekurencyjną.

"""

def odwracanie(L, left, right):
    b = L[left:right]
    b.reverse() 
    suma = L[:left]  + b + L[right:]
    print (suma)
    return


lista = [1,2,3,4,5,6,7,8,9,10] 
r = 8
l = 3
odwracanie(lista, l, r)