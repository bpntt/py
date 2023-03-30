""" list1=[]
totalplayers = int(input('total: '))
def filllist ():
    count = 0
    while count<0:
        count+=1 """
list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

list_difference = []
for element in list_1:
    if element not in list_2:
        list_difference.append(element)

print(list_difference)