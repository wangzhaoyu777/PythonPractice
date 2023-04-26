# Zhaoyu Wang developed
# time: 2023-04-25 8:41 p.m.


# 准备列表
my_list = [['a',33],['b',55],['c',11]]
# 排序基于带名字的函数
# def choose_short_key (element):
#     return element[1]
# my_list.sort(key=choose_short_key, reverse=False)
# print(my_list)
# 排序用lambda
my_list.sort(key=lambda element : element[1], reverse=True)

print(my_list)