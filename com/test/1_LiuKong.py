# -*- coding: utf-8 -*-
score = 15
if score > 60:
    print ('及格')
    print ('及格')
else:
    print('不及格')
    
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print(name)
    
N = 10
x = 0
while x < N:
    print (x)
    x = x + 1
    
    
for xe in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print (xe + y)
        

map = {
    'name':'张三',
    'age' :'222'
        
}

print(map['name'])

map['kk'] = 28
map['nmae'] = '1111'
print(map['kk'])
print(map['name'])


print('')

for key in map:
    print(key)
    
    
s = set(['A', 'B', 'C'])
print(s)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-1100))