#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. 
#Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
print('podaj zdanie: ')
line = input()
line = line.replace('\\t', '\t').replace('\\n', '\n')
x = line.split()
slowo=("twoje slowo z pierwszych wyrazow to: ")
owols=("twoje slowo z ostatnich wyrazow to: ")
for val in x:
    slowo=slowo+val[0]
    owols=owols+val[-1]
print(slowo)
print(owols)
