dig = int(input('write a number: '))
def check (a):
    if 0<a<10:
        a=a*a
        print(a)
    else: print('wrong number! The number cannot be bigger then 10 and less then 0')
check(dig)