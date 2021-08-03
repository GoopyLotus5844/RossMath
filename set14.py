import nt_helpers as nt

'''
n = 5
for p in nt.list_primes(10000):
    test = p % n == 1
    square = len(nt.square_roots(p, n)) > 0
    if test and not square: print('statement false')
    if not test and square: print('converse false')
    '''

def norm(a, b, c):
    return a ** 3 + 2 * b ** 3 + 4 * c ** 3 - 6 * a * b * c


r = 20
for a in range(-r, r):
    for b in range(-r, r):
        for c in range(-r, r):
            if norm(a, b, c) == 31*31: print(a, b, c)
