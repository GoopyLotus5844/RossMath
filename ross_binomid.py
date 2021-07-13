def sequence(n):
    return (4) ** n + 1

def calc_bin(n, k):
    numerator, denominator = 1, 1
    for x in range(n - k + 1, n + 1): numerator *= sequence(x)
    for x in range(1, k + 1): denominator *= sequence(x)
    return numerator / denominator

for n in range(1, 10):
    for k in range(1, n + 1):
        print((n, k), calc_bin(n, k))