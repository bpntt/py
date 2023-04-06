list1 = [1,2,3,4,5]
print(list1)
k = int(input('write your number'))
a = k%len(list1)
for i in range(k):
    num = list1.pop(-1)
    list1.insert(0,num)
print(list1)