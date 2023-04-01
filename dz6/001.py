a =int(input('write first eliment: '))
b = int(input('range: '))
c = int(input('total dig: '))
def genirator(a,b,c):
    for i in range(c):
        if i < c:
            print(a + i * b, end=' ')
            i+=1
genirator(a,b,c)