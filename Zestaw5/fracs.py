"""
Zadanie 2 - Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. 
Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.

"""
import math

def add_frac(frac1, frac2): 
    x = frac1[0]*frac2[1] + frac2[0]*frac1[1]
    y = frac1[1]*frac2[1]
    d = math.gcd(x,y)
    frac3 = [(x/d),(y/d)]
    return frac3            # frac1 + frac2

def sub_frac(frac1, frac2): 
    x = frac1[0]*frac2[1] - frac2[0]*frac1[1]
    y = frac1[1]*frac2[1]
    d = math.gcd(x,y)
    frac3 = [(x/d),(y/d)]
    return frac3            # frac1 - frac2

def mul_frac(frac1, frac2): 
    x = frac1[0]*frac2[0]
    y = frac1[1]*frac2[1]
    frac4 = [x,y]
    d = math.gcd(x,y)
    frac3 = [(x/d),(y/d)]
    return frac3             # frac1 * frac2

def div_frac(frac1, frac2):
    x = frac1[0]*frac2[1]
    y = frac1[1]*frac2[0]
    frac4 = [x,y]
    d = math.gcd(x,y)
    frac3 = [(x/d),(y/d)]
    return frac3               # frac1 / frac2

def is_positive(frac): 
    if frac[0]*frac[1] < 0:
        x = bool(0)
    else : 
        x = bool (1)            # bool, czy dodatni
    return x

def is_zero(frac): 
    if frac[0] == 0:
        x = bool(1)
    else: 
        x = bool(0)        # bool, typu [0, x]
    return x

def cmp_frac(frac1, frac2):
    x = frac1[0]*frac2[1]
    y = frac1[1]*frac2[1]
    frac3 = [x,y]
    a = frac2[0]*frac1[1]
    b = frac2[1]*frac1[1]
    frac4 = [a,b]
    if frac3 == frac4:
        return 0
    elif frac3 < frac4:
        return 1
    else: 
        return -1       # -1 | 0 | +1

def frac2float(frac): 
    x = float(frac[0]/frac[1])    
    return x        # konwersja do float

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([4, 5],[3, 8]), [47,40])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([1,2],[2,3]), [-1,6])
        self.assertEqual(sub_frac([5,8],[3,8]), [1,4])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1,2],[2,4]), [1,4])
        self.assertEqual(mul_frac([1,5],[5,1]),[1,1])

    def test_div_frac(self): 
        self.assertEqual(div_frac([2,6],[1,2]), [2,3])
        self.assertEqual(div_frac([4,2],[1,1]),[2,1])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1,2]),False)
        self.assertEqual(is_positive([1,6]),True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0,1]),True)
        self.assertEqual(is_zero([1,3]),False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,2],[2,3]),1)
        self.assertEqual(cmp_frac([8,9],[7,9]),-1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1,2]),0.5)
        self.assertEqual(frac2float([1,4]),0.25)

    def tearDown(self):
        del self.zero

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy