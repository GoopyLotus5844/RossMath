import nt_helpers as nt

for p in nt.list_primes(30):
    roots = False
    for x in range(p):
        if (x ** 2 + 1) % p == 0:
            roots = True
    if not roots: print(p, "has no roots")

print(nt.order(61, 40))