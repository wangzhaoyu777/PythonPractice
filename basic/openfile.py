# Zhaoyu Wang developed
# time: 2023-03-27 9:52 p.m.

# file = open('a.txt','r')
# print(file.read(2))
# file.close()

file = open('c.txt', 'a')
lst = ['a\n', 'b\n', 'c']
file.writelines(lst)
file.close()


