import datetime
a = datetime.datetime.now()
"""def sum1(number):
    sum1, i = 1, 2
    while i*i < number:
        if number % i == 0:
            sum1 += i
            sum1 == (number//i)
        i += 1
    return sum1


k, i = 100000, 1
while i < k:
    j = sum1(i)
    if i < j < k and i == sum1(j):
        print(f'{i} {j}') """


def sum_div(num):
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += 1
    return sum_


k = 300
for num1 in range(2, k):
    num2 = sum_div(num1)
    sumnum2 = sum_div(num2)
    if (sumnum2 == num1) and (num1 != num2) and (num1 < num2):
        print(num1, num2)
print(datetime.datetime.now() - a)
