import nt_helpers as nt
import math

for x in range(1, 10):
    print(x, math.factorial(x - 1) % x)