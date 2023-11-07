a = [1, 5, 2, 8]
b = a
b[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()
c = [1, 4, 2, 5]
d = c[:]
d[3] = 0
print(f'Lista C: {c}')
print(f'Lista D: {d}')
