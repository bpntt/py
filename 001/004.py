a = float(input('write you int: '))
f=1
while a > 1:
    f *= a
    a -= 1
    break
    print(f)
else:
    while a < 0:
        f = 1
    f *= a
    a += 1
    print(f)
""" не смог придумать как работать с отрицательными значениями  """