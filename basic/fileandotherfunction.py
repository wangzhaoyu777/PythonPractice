# Zhaoyu Wang developed
# time: 2023-03-27 9:52 p.m.
import os
# file = open('a.txt','r')
# print(file.read(2))
# file.close()

# file = open('a.txt', 'r')
# # lst = ['a\n', 'b\n', 'c']
# file.seek(4)
# print(file.read())
# # file.writelines(lst)
# file.close()
# print('------------------------------------------')
# file = open('b.txt', 'r')
# file.seek(0)
# print(file.read())
# print(file.tell())
# file.close()
# os.system('calc')
# os.system('notepad')
# os.startfile('C:\\steam\\steam.exe')
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)


