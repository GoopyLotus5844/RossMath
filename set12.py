import nt_helpers as nt

for n in range(1, 1000):
    if sum([nt.phi(d) for d in nt.list_divisors(n)]) != n: print(n)

for n in range(1, 20):
    print(n, [str(d) + ": " + str(nt.phi(d)) for d in nt.list_divisors(n)])
