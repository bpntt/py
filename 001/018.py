a = [1, 2, 3, 4, 5, 6]
""" res = list()

for i in a:
        if i % 2 == 0:
            res.append((i, i**2))
            i+=1
        else: i+=1
print(res) """


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


res = select(int, a)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
