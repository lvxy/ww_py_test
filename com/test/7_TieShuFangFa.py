# -*- coding: utf-8 -*-
'''
Created on 2016年9月27日

@author: Administrator
'''

#特殊方法
#__str__
#__len__
#__cmp__

class Person(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '{persion:{ name:%s,gender:%s}}' % (self.name, self.gender)
    

p = Person("张三","男")

p.nnnnn = 1111# 回报错__slots__制定允许属性列表
print(p)

#函数也是对象，对象和函数的区别并不显著
