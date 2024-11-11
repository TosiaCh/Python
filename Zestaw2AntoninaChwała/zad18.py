#Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

liczba=12309873027300
y=str(liczba)
lista=list(y)
print(lista)
count=0
for e in lista:
    if e=='0':
        count = count + 1
print('Jest '+str(count)+' zer w liczbie '+y)
