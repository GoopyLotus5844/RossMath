from fractions import Fraction

def test(val, total):
    angle = 0
    counter = 0
    while True:
        angle += val
        counter += 1
        angle %= total
        if angle == 0: break
        if total % angle == 0:
            print(val, angle, counter)
            return False
    return True

total = 360
for x in range(1, 2*total):
    if(test(x, total)): print('holy crap')


#print(test(Fraction(17, 19)))
    