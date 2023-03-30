from random import randint
a = int(input('write frirs len: '))
b = int(input('write seckond len: '))
list_1 =[]
list_2=[]
def random_list(a,list_3):
    for i in range(a):
        list_3.append(randint(0,10))
random_list(a, list_1)
random_list(a, list_2)
print(list_1)
print(list_2)
list_diffirence = []
def fibnd(a,b):
    for element in a:
        if element not in b:
            list_diffirence.append(element)
fibnd(list_1,list_2)
print(list_diffirence)