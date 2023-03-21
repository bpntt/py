import random
dig1 = int(input('write your number'))


def rnd(n, c):
    p = 0
    q = 0
    while p < n:
        a = random.randint(0, 5)
        p += 1
        print(a, end=" ")
        if a == c:
            q += 1
    print('\n')
    print(q)


rnd(10, dig1)
