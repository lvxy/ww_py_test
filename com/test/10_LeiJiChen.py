# -*- coding: utf-8 -*-
import json

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    



class Studet(Person):
    def __init__(self,name,gender,school,score):
        super(Studet,self).__init__(name, gender)
        self.school = school
        self.score = score
        

stu1 = Studet("张三","男","上海交大",98)

print(stu1.name)
print(stu1.gender)
print(stu1.school)
print(stu1.score)   



print(isinstance(stu1, Person))   


