import nt_helpers as nt

n = 7
for x in nt.list_units(n):
    print(x, nt.order(n, x))
