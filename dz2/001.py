import random 
n = int(input('count10'))
def rnd (n):
    a = 0 
    p= 0
    q= 0
    w = 0
    while p < n :
        a = random.randint(0,1)
        if a == 0 : q+=1
        else : w+=1 
        p +=1
        print (a, end=" ")
    if q>w : return print('change b')
    else : return print ('change a')
rnd(n)
