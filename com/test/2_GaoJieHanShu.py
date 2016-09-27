# -*- coding: utf-8 -*-
#高阶函数
import math

def maxx(x,y):
    if(x >= y):
        return x
    if(x < y):
        return y
    
def add(x,y,f):
    return f(x)+f(y)

print(add(2,5,abs))

print(math.sqrt(7))



def f(x):
    return x*x
vv = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for v in vv:
    print(v)



def is_not_empty(s):
    return s and len(s.strip()) > 0
ll = ['test', None, '', 'str', '  ', 'END']
ll = filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

for l in ll:
    print(l)


def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r == x

tt = filter(is_sqr,range(1,100))

for t in tt:
    print(t)
    
    
#装饰器 函数 @log@transaction@post('regin')
def log(f):
    def fn(x):
        print('call '+f.__name__+"()")
        return f(x)
    return fn

@log
def f1(x):
    return x*2

print(f1(10))


        