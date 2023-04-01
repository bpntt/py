from random import randint

a = int(input('write first nimber: '))
b = int(input('write second nimber: '))
c = int(input('write the list length: '))
list_1 = []
list_2 = []
def random_list(a, list_1):
    for i in range(a):
        list_1.append(randint(-10, 10))
def list_total (list_2,list_1, b,c):
    for i in range(len(list_1)):
        if b <= list_1[i] <= c:
            list_2.append(list_1[i])
            i+=1

random_list(c, list_1)
list_total(list_2,list_1, a, b)
print(list_1)
print(list_2)