import nt_helpers as nt

p = 10
a = 4
r_list = []
for j in range(1, p):
    r_list.append(a * j % p)
print(r_list)
