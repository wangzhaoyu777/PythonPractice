# Zhaoyu Wang developed
# time: 2023-03-21 3:18 p.m.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(self.name+' eating')
#
#     @staticmethod
#     def staticMethod():
#         print('sm')
#
#     @classmethod
#     def cm(cls):
#         print('cm')
# stu1 = Student('John', 20)
# stu1.eat()
# Student.cm()
# stu1.cm()
# print(stu1.name)
# print(stu1.age)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
    def info(self):
        print(self.name, self.age, self.stu_no)
    def __add__(self, other):
        return self.name + other.name

class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name,age)
        self.teachosyear = teachofyear
    def info(self):
        print(self.name, self.age, self.teachosyear)
#
stu1 = Student('a', 20, 123)
stu2 = Student('b', 20, 123)
# teacher1 = Teacher('b', 31, 2)
# print(stu1.__dict__)
s = stu1 + stu2
print(s)
print('tt')
print('push test')