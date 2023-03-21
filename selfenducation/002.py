age = int(input('how old are you? '))
weight = int(input('what is your weight?'))


def healthcheck(a, b):
    if a < 30:
        if 50 < b < 120:
            print('well health')
        else:
            print('your need a healthcheck')
    if 40 > a > 30:
        if 50 > b or b > 120:
            print('your need a healthcheck')
        else:
            print('well health')
    if a > 40:
        if 50 > b or b > 120:
            print('your need a healthcare')
        else:
            print('well health')


healthcheck(age, weight)
