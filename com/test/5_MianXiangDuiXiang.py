# -*- coding: utf-8 -*-
'''
Created on 2016��9��26��

@author: Administrator
'''

class Person(object):
    
    count = 0
    
    def __init__(self, name, gender, birth):
        Person.count = Person.count + 1
        
        self.name = name
        self.gender = gender
        self.birth = birth

xiaoMing = Person('小明', 'Female', '1992-2-2')
xiaoHui = Person('小明', 'Female', '1992-2-2')

print(xiaoMing.name+ ' ' +xiaoMing.gender)
