import math

squares = []
cubes  = []
fourths = []
mod = 29

for x in range(29):
    s, c, f = (x ** 2) % mod, (x ** 3) % mod, (x ** 4) % mod
    if not(any(t[1] == s for t in squares)): squares.append((x, s))
    if not(any(t[1] == c for t in cubes)): cubes.append((x, c))
    if not(any(t[1] == f for t in fourths)): fourths.append((x, f))

def order(m, a):
    if math.gcd(m, a) != 1: return -1
    k = 1
    while True:
        if (a ** k) % m == 1: return k
        k += 1

print(squares, len(squares))
print(cubes, len(cubes))
print(fourths, len(fourths))