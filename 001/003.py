a = int(input('write you int: '))
if a == 0: a = 1
f = 1
while a > 1:
    f *= a
    a -= 1

print(f)