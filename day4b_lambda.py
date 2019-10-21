a = [333, 4444, 1, 22, ]
print(f'a={a}')

a.sort()
print(f'a={a}')

a = [5, 66, 333, 4444, 1, 22, 777, 8888]
#a.sort(key=lambda x,y: x>=y) #TODO custom comparator?

a = [
    {'x': 4444,  'y': 22},
    {'x': 1,  'y': 55},
    {'x': 22, 'y': 223},
]
print(f'a={a}')
a.sort(key=lambda item: item.get('x'))
print(f'a={a}')
