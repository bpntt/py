a = int(input('write int: '))
a =int(a)
b =0
while 2 ** b < a:
        f = 2 **b
        b+=1
        print(f, end=' ')