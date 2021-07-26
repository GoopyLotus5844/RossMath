import nt_helpers as nt
import math

'''
ord = 5
count = 0
mod = 31

for x in range(1, mod):
    if nt.order(mod, x) == ord:
        count += 1
        print(x)

print(nt.phi(ord), count)
'''

'''
for x in range(2, 50):
    print(x, math.factorial(x - 1) % x)

for x in nt.list_primes(13):
    print((math.factorial(x - 1) + 1) / x)
'''

'''
mod = 7
for x in range(1, mod):
    for y in range(1, mod):
        r, s = nt.order(mod, x), nt.order(mod, y)
        lcm = math.lcm(r, s)
        order = nt.order(mod, x * y)
        if math.lcm(r, s) == 1 and order != r * s:
            print("first conjecture broken")
        if order != lcm:
            print(x, y, r, s, order, lcm)
'''

for m in range(50):
    for x in range(1, m):
        if math.gcd(x, m) != 1:
            found = False
            for y in range(1, m):
                if x != y and (x * y) % m == 0:
                    found = True
                    break
            if not found:
                print(m, x)
        
