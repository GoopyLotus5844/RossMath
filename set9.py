import nt_helpers as nt

n = 9
for x in nt.list_units(n):
    print(x, nt.order(n, x))

print(nt.phi(27))
