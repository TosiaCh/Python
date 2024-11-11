#Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe 
# będą miały blok dopełniony zerami, 
#np. 007, 024. Wskazówka: str.zfill().

L=[22,1,987,21,5,314]
z=0
for e in L:
    x=str(e).zfill(3)
    L[z]=x
    z=z+1
print(L)
print(''.join(str(e) for e in list (L)))
   