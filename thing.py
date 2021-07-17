def check(a, b, c, d):
    k1 = (a * c) % 5
    k2 = (a * d + b * c) % 5
    k3 = (b * d) % 5
    return k1 == 1 and k2 == 1 and k3 == 1

for a in range(5):
    for b in range(5):
        for c in range(5):
            for d in range(5):
                if check(a, b, c, d): print('wow') 

print('done')