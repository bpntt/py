
transfomation = lambda item: item
values = [1,2,'asdfg']
transformed_values = list(map(transfomation, values))
if values == transformed_values:
    print('ok')
else: 
    print('fail')