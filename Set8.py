import nt_helpers

'''
for x in range(105):
    if x * x % 105 == 4: print(x)
'''

'''
print(nt_helpers.list_powers_of(61, 2))
print(nt_helpers.order(61, 2))
print(nt_helpers.list_perfect_powers(61, 8))
print(nt_helpers.phi(20))
'''

'''
results = []
for x in range(1, 21):
    results.append((x, nt_helpers.phi(x)))
'print(results)'
'''

'''
for x in range(3, 101, 2):
    order = nt_helpers.order(x, 2)
    print(x, order)
'''

for x in nt_helpers.list_primes(100):
    if not nt_helpers.is_generator(x, 2): print(x)

