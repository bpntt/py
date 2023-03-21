import random
len1 = int(input('write length'))


def rnd(n):
    a = 0
    p = 0
    q = 0
    while p < n:
        a += 1
        p += 1
        print(a, end=' ')
    print('\n')
    print(a-1)


rnd(len1)
