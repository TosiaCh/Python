"""
ZADANIE 7 - Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, 
wykonać przez isinstance(item, (list, tuple)).

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]

"""
def flatten(sequence):
    wynik = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            wynik = wynik + flatten(i)
        else:
            wynik.append(i)
    return wynik

seq = [2,3,4,[2,3],[2,3,[4,3,[4]],3,4],7]
print(seq)
print(flatten(seq))