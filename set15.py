import nt_helpers as nt

'''
def poly1(m, x):
    return (x ** 2 - 1) % m

def poly2(m, x):
    return (x ** 2 + x - 6) % m

def poly3(m, x):
    return (x ** 3 - 1) % m

def R(m, poly):
    return [x for x in range(m) if poly(m, x) == 0]

p, q, k1, k2, poly = 2, 7, 3, 5, poly1
print(R(p ** k1, poly), R(q ** k2, poly), R(p ** k1 * q ** k2, poly))
print(len(R(p ** k1, poly)) * len(R(q ** k2, poly)) == len(R(p ** k1 * q ** k2, poly)))
'''

'''
def sigma(k, n):
    return sum([d ** k for d in nt.list_divisors(n)])

a, b, k = 4, 6, 2
print(sigma(k, a), sigma(k, b), sigma(k, a * b))
'''

for p in nt.list_primes(10000):
    test = p % 12 == 1 or p % 12 == 11
    square = len(nt.square_roots(p, 3)) > 0
    if test and not square: print('not square', p)
    if square and not test: print('not test', p)
