"""
ZADANIE 4 - Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

"""
def fibonacci(n):
    if n==0:
        return print(0)
    elif n==1:
        return print(1)
    else:
        L=[]
        L.append(0)
        L.append(1)
        for i in range(2,n+1):
            L.append(L[i-1]+L[i-2])
        return print(L[-1])
fibonacci(0)
fibonacci(1)
fibonacci(3)
fibonacci(4)
fibonacci(20)
fibonacci(6)

