import nt_helpers as nt

print(nt.is_generator(73, 5))

print(nt.list_powers_of(73, 5))

for x in range(73):
    if (x ** 29) % 73 == 7: print(x)

print(nt.order(73, 17))