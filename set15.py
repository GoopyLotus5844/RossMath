import nt_helpers as nt

def poly1(m, x):
    return (x ** 2 - 1) % m

def poly2(m, x):
    return (x ** 2 + x) % m

def poly3(m, x):
    return (x ** 3 - 1) % m

for p in nt.list_primes(10):
    for k in range(1, 10):
        m = p ** k
        print(m, [x for x in range(m) if poly3(m, x) == 0])