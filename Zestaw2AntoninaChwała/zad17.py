#Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. 
#Wskazówka: funkcja wbudowana sorted().

line='kofkk ekok eokoe'
print(line)
y=sorted(line.split(),key=str.casefold)
print('alfabetycznie: ')
print(y)
l=line.split()
z=sorted(l,key=len)
print('długościowo: ')
print(z)
