from random import randint
list_1 =[]
def digts():
    while True:
        s = input('Whrite your int between 0 and 1000 ')
        try:
            n = int(s)
            if 0 < n and n < 1001:
                break
            else:
                print('Wrong int')
        except:
            if s.isalpha():
                print("IS IT WORD?!")
            else:
                print(f"%%#??")
    s = int(s)
    return s

def random_list(a,list_1):
    for i in range(a):
        list_1.append(randint(0,1000))
        if list_1[i] == 0:
            return print(max(list_1))
        else: 
            i+=1

random_list(digts(), list_1)
print(list_1)


