import math

def list_powers_of(m, a):
    powers, current, k = [], a, 1
    while True:
        powers.append((k, current))
        if current == 1: return powers
        current = (current * a) % m
        k += 1

def list_perfect_powers(m, k):
    powers = []
    for x in range(1, m):
        power = (x ** k) % m
        if not(any(t[1] == power for t in powers)): powers.append((x, power))
    return powers

def order(m, a):
    if math.gcd(m, a) != 1: return -1
    return len(list_powers_of(m, a))

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def is_generator(m, k):
    return order(m, k) == phi(m)

def prime_table(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime

def list_primes(n):
    return [i for i, val in enumerate(prime_table(n)) if val]

def list_units(m):
    return [i for i in range(1, m) if math.gcd(i, m) == 1]