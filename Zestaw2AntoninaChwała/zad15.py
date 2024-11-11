#Na liście L znajdują się liczby całkowite dodatnie. 
#Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
L= [1,2,3,4,5,6]
print(L)
z=''.join(str(e) for e in list (L))
print(z)

