def digts():
    while True:
        s = input('Whrite your int between 0 and 1000 ')
        try:
            n = int(s)
            if 0 < n and n < 1000:
                break
            else:
                print('Wrong int')
        except:
            if s.isalpha():
                print("IS IT WORD?!")
            else:
                print(f"%%#??")
    return s


def getback(s, p):
    y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
    x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
    return y1, x1


a = int(digts())
b = int(digts())
s = a+b
p = a*b
print(f'Sum =  {s}, Sqr = {p}')
print(getback(s, p))
