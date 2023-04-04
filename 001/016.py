a = int(input('write first nimber: '))
b = int(input('write second nimber: '))
list_1 = []
list_2 = []

def find(a, list1):
    sum1 = 0
    b = 1
    while b <= a and b != a:
        if a % b == 0:
            sum1 = sum1+b
            b += 1
            list1.append(sum1)
        else:
            b += 1


def check(a, list_3):
    c = 0
    for i in range(len(list_3)):
        if list_3[i] == a:
            c = 1
        else:
            i += 1
    return c 


def final_check(a, b):

    if a > 0 and b > 0:
        print('Given numbers are Amicable!')
    else:
        print('Given numbers are not Amicable!')


find(a, list_1)
find(b, list_2)
""" print(list_1)
print(list_2) """
final_check(check(b, list_1), check(a, list_2))
