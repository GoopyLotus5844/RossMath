from fractions import Fraction

f = Fraction(723, 2)
f %= 360
print(f)

print(360 % Fraction(17, 19))