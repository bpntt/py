# size = int(input('size'))
# a = int(input('first number'))
# b = int(input('second number'))
# d = int(input('find'))
# f = 0
# c = 0
# while c< size:
#     f = a+b
#     a=b
#     b=f
#     c+=1
#     print(b, end=" ")
# if f == d : print(c)
# else : print('-1')



# size = int(input('size'))
# c = 2
# a = int(input('first number'))10

# b = int(input('second number'))
# d = int(input('find'))
# f = 0
# text = 0
# while c < size:
#     f = a+b
#     a = b
#     b = f
#     c += 1
#     text= b, end=" "

# print(text.find(d))
# Не знаю как сделать так что бы работало. хочу что бы при ошбке просто выводило нет или просто да без перегонки по кругу для каждого числа
#   """

# """ size = int(input('size'))
# a = int(input('first number'))
# b = int(input('second number'))
# d = int(input('find'))
# f = 0

# def fillarray(a,b,size):
#     arr = []
#     arr [0] =  a
#     arr[1] = b
#     for i in range(size):
#         arr[i] = arr [i-1] + arr[i-2]
#     return arr
# print(fillarray(a,b,size))
size = int(input('size'))
a = int(input('first number'))
b = int(input('second number'))
d = int(input('find'))
f = 0
c = 0
arra = []
def arrFib(a,b,n):
    res=[]
    p=a
    c=b
    for i in range(n):
        res+=[c]
        c,p=c+p,c
    return res
def find ():
    i = 0
    for i in range(len):
        if arra[i] == d : return print('ture')
        else : return print('-1')
print(str(arrFib(a,b, size)))
print(str(find(arrFib(a,b,size))))
