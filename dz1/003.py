a = int(input('Write your tickets number(6dig)'))
b = a//1000
c = b // 100
d = b // 10 % 10
e = b % 10
f = a % 1000
g = f // 100
h = f // 10 % 10
l = f % 10
print('true' if (c+d+e == g+h+l) else 'false')
