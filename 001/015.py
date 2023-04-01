from random import randint
a = int(input('write first nimber: '))
b = int(input('write second nimber: '))
list_1 = []
list_2 = []


def find(a, b):
    difference_1 = set(list_1).difference(set(list_2))
    difference_2 = set(list_2).difference(set(list_1))
    list_difference = list(difference_1.union(difference_2))
    return print(list_difference)


def random_list(a, list_1):
    for i in range(a):
        list_1.append(randint(0, 10))


random_list(a, list_1)
random_list(b, list_2)
print(list_1)
print(list_2)
print()
find(list_1, list_2)