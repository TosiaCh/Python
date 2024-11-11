"""
ZADANIE 1
x = 2; y = 3
if (x > y):
    result = x
else:
    result = y
ODP: w pythonie nie używamy średników chyba że definujemy kilka zmiennych w jednej linijce
nawiasy są opcjonalne (przy warunku)

for i in "axby": if ord(i) < 100: print (i) --> ta linijka nie jest poprawna if wymaga składni składającej 
się z wcięć

for i in "axby": print (ord(i) if ord(i) < 100 else i) --> to wyrażenie jest poprawne po for występuje print
a dopiero w nim zawarty jest if else, który nie wymaga składni

"""
"""
ZADANIE 2
L = [3, 5, 4] ; L = L.sort() --> tutaj my nie zamieniamy L na L posortowane tylko próbujemy je porównać to błąd
x, y = 1, 2, 3 --> próba dopasowania do 2 zmiennych 3 wartości to błąd
X = 1, 2, 3 ; X[1] = 4 --> X nie jest listą więc nie możemy zmieniać jej wartości dla 1 indeksu
X = [1, 2, 3] ; X[3] = 4 --> nie ma indeksu 3 więc nie zadziała
X = "abc" ; X.append("d") --> X to string więc nie tak dodaje się watrości moglibyśmy tu uzycj jakiegoś join
L = list(map(pow, range(8))) --> funkcji pow brakuje argumentu

"""

"""
ZADANIE 3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

"""

for i in range(30):
    if i%3 != 0:
        print(i)

"""
ZADANIE 4 Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
i wypisujący x oraz trzecią potęgę x.
Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie 
i kontynuować pracę.

"""
while True:
    try:
        x = input("Podaj liczbę rzeczywistą: ")
        if(str(x) == "stop"):
            break
        y = float(x)
        print(y)
        print(y**3)
    except ValueError:
        print("Error! Miała być l. rzeczywista :(")

"""
ZADANIE 5 Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr 
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
Należy zbudować pełny string, a potem go wypisać.

"""
    
x=int(input("Podaj długość dla miarki: "))
L=[]
M=[]
for i in range(x):
    L.append(str("|...."))
    if i<8:
        M.append(str(i+1)+ "    ")
    else:
        M.append(str(i+1)+"   ")
L[-1]="|"
S="".join(L)
J="".join(M)
nowe= S + "\n" + J
print(nowe)

"""
ZADANIE 6 Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać.Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+

"""
x=input('Podaj wymiary (przykład 2 4): ')
y=x.split()
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
print(nowe)
# czyszczenie list 
L.clear()
M.clear()
K.clear()
O.clear()
P.clear()
"""
ZADANIE 8 Dla dwóch sekwencji liczb lub znaków znaleźć: 
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

"""
x="12345kjd"
y="1k890p4dmn"
print('Sekwencja 1: '+x)
print('Sekwencja 2: '+y)
a=' '.join(x)
L=a.split()
b=" ".join(y)
M=b.split()
# A
for i in L:
    for j in M:
        if j == i:
            if j not in O:
                O.append(j)
print('Lista w obu sekwencjach: ')
print(O)
# B
for a in L:
    if a not in P:
        P.append(a)
for b in M:
    if b not in P:
        P.append(b)
print('Lista wszystkich znaków: ')
print(P)

"""
ZADANIE 9 Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

"""
print('ZADANIE 9')
L=[[],[4],(1,2),[3,4],(5,6,7)]
O=[]
for i in L:
    x=sum(i)
    O.append(x)
print(O)

"""
ZADANIE 10 Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
(z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

#sposób 1
x=input('Podaj liczbę w systemie rzymskim: ')
y=' '.join(x)
L=[]
L=y.split()
slownik = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
slownikv2 = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100),('D', 500), ('M', 1000)])
slownikv3 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
print(L)

def roman2int(x):
    M=[]
    suma = 0
    for i in x:
        value=slownik[i]
        M.append(value)
    print (M)
    last_item = 0
    for i in M:
        if last_item < int(i):
            suma = suma - last_item
            last_item = int(i)
        else:
            suma = suma + last_item
            last_item = int(i)  
        
    suma = suma + M[-1]
    print(suma)

roman2int(L)