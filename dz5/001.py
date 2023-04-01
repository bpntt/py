a = int(input('write first nimber: '))
b = int(input('write second nimber: '))


def squd(a, b):
    if b == 0:
        return 1
    else:
        return a * squd(a, b - 1)


print(squd(a, b))