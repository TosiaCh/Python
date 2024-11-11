#Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

print('Napisz coś, a ja policzę z ilu liter składa się słowo!')
line = input()
line = line.replace('\\t', '\t').replace('\\n', '\n')
x = line.split()
y="".join(x)
suma=len(y)
print('Twoje słowo składa się z '+ str(suma) +' liter')
