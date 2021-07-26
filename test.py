import nt_helpers as nt

print(nt.square_roots(5, 2))
print(nt.square_roots(5, 3))

for x in range(1, 105):
    if ((x ** 4) - 4) % 105 == 0: print(x)