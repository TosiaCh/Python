
"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, 
tylko korzystać z argumentów.

"""



"""
ZADANIE 5 Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr 
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
Należy zbudować pełny string, a potem go wypisać.

"""
def miarka(dlugosc):    
    L=[]
    M=[]
    for i in range(dlugosc):
        L.append(str("|...."))
        if i<8:
            M.append(str(i+1)+ "    ")
        else:
            M.append(str(i+1)+"   ")
    L[-1]="|"
    S="".join(L)
    J="".join(M)
    nowe= S + "\n" + J
    return print(nowe) 
miarka(7)
"""
ZADANIE 6 Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać.Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+

"""
def kwadrat(dlugosc):

    y=dlugosc.split()
    n=y[0] #pion
    z=y[1] #poziom
    O=[]
    P=[]
    for i in range (int(z)):
        O.append("+---")
        P.append('|   ')
    O.append('+')
    P.append('|')
    S=''.join(O)
    J=''.join(P)
    K=[]
    for i in range (int(n)):
        K.append(S + "\n" + J + "\n")
    nowe = ''.join(K) + S
    
    return print(nowe)
kwadrat('7 3')