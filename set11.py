import nt_helpers as nt

'''
for p in nt.list_primes(30):
    roots = False
    for x in range(p):
        if (x ** 2 + 1) % p == 0:
            roots = True
    if not roots: print(p, "has no roots")

print(nt.order(61, 40))

check = [2, 5, 37, 9, 17, 7, 23]
for n in check: 
    print((n ** 52) % 105, nt.square_roots(105, n))
'''

for m in nt.list_primes(20):
    for x in range(1, m):
        square = len(nt.square_roots(m, x)) > 0
        test = (x ** ((m - 1) / 2)) % m == 1
        if square and not test: print('case1', m, x)
        if test and not square: print ('case2', m, x)
