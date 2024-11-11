"""
ZADANIE 6 - Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, 
a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

"""

def sum_seq(sequence):
    suma = 0
    for i in sequence:
        if isinstance(i,(list, tuple)):
            lista=i
            suma = suma + sum_seq(lista)
        else: 
            suma = suma + i
    return suma
            


seq = [1,1,1,1,[1,1,1,1],1,1,[1,1,1],1,[1,1,[1,1]]]
prawdziwa_Suma = 18
print(sum_seq(seq))
