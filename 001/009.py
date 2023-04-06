str = list(input('write your text: ').split())
count = 0
for i in range(len(str)):
    if i< len(str):
        count+=1
print(count)