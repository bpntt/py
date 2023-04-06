str = ("a a a a a a b c d d d d d d d d c c ").split()
dict ={}
for i in str:
    if i not in dict:
        dict[i]= 0
        print(i, end=' ')
    elif i in dict:
        dict[i]+=1
        print(f'{i}_{dict[i]}', end=" ")
