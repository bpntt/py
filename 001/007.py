list_1 = [1,3,5,2,1]
count = 0
for i in range(1, len(list_1)):
    if list_1[i]<list_1[i-1]:
        count+=1
if count >0:
    print(count)
else:
    print('0')