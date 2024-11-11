#Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
print('Napisz coś, a ja znajdę najdłuższy wyraz i jego długość!')
line = input()
line = line.replace('\\t', '\t').replace('\\n', '\n')
x = line.split()
y=0
for val in x:
    if y<len(val):
        y=len(val)
        z=val
print('najdłuższe słowo to '+z)
print('ma długość '+ str(y) )