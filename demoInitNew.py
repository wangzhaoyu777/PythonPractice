# Zhaoyu Wang developed
# time: 2023-03-25 9:28 p.m.
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('new 被调用了，cls的ID值为:{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建对象的id为:{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('init bei调用了，self的ID的值为:{0}'.format(id(self)))
        self.name = name
        self.age = age
print('obj这个类的对象的id:{0}'.format(id(object)))
print('Person这个类的对象是:{0}'.format(id(Person)))

p1 = Person('a', 20)
print('p1这个对象的id为:{0}'.format(id(p1)))



