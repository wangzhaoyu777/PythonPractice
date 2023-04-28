# Zhaoyu Wang developed
# time: 2023-04-27 8:14 p.m.
import random
class Phone:
    producer = 'joeyW'
    __is_5g_enable = True

    def test(self):
        print('t')
    def __check_5g(self):
        if self.__is_5g_enable:
            print('5g开启')
        else:
            print('5g关闭使用4g')
    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中')

class Phone2023(Phone):
    producer = 'zhaoyuW'
    def test(self):
        print('1234')

random.randint(1,10) # type: int
phone = Phone()
phone.test()
print(phone.producer)