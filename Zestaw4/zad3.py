"""
ZADANIE 3 - Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

"""
def factorial(n):
    x=1
    if n==0:
        return print(0)
    else:
        for i in range (n):
            x*=i+1
    return print (x)
factorial(1)
factorial(2)
factorial(5)
factorial(20)
factorial(0)


