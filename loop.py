# Zhaoyu Wang developed
# time: 2023-03-17 11:13 a.m.
#
# print(bool(False))
# print(bool(0))
# print(bool(0.0))
# print(bool(''))
# print(bool(None))
# print(bool([]))
# print(bool(list()))
# print(bool({}))
# print(bool(dict()))
# print(bool(()))
# print(bool(set()))
# print(bool(tuple()))
# print("----------------------all false above, all other bool are true---------------")
#
# num = input("type a number ")
# if int(num) % 2 == 0:
#     print('is even')
# else:
#     print(' is odd')
#
# num = int(input("输入你的分数"))
# if num < 0 or num > 100:
#     print("你是不是扯呢？？🙄🙄🙄")
# else:
#     pass
#
# if 100 >= num >= 90:
#     print("分段 A 牛的兄弟🎉🎉🎉")
# elif 89 >= num >= 80:
#     print("分段 B 也不错✨")
# elif 79 >= num >= 70:
#     print("分段 C 一般吧😑")
# elif 69 >= num >= 60:
#     print('D 有点水啊，得加油了🙃')
# elif 60 > num >= 0:
#     print('E 你干鸡毛了你？？？😤😤😤')
# print(-----------------------------------------------------------)
#
# status = input("是否是会员 y or n")
#
# if status == "y" or status == "n":
#     pass
# else:
#     print("error")
# num = float(input('消费多少钱'))
# if status == 'y':
#
#     if num >= 200:
#         print('这次消费' + str(num * 0.8) + '下次再来金主爸爸')
#     elif 200 > num >= 100:
#         print("这次消费" + str(num * 0.9) + "下次再来金主爸爸")
#     else:
#         print("这次消费" + str(num) + "下次再来金主爸爸")
# else:
#
#     if num >= 200:
#         print("这次消费" + str(num * 0.95) + "办个会员啊")
#     else:
#         print("这次消费" + str(num) + "办个会员啊")
# r = range(12)
# print(r)
# print(list(r))
# r = range(1, 12)
# print(r)
# print(list(r))
# r = range(1, 12, 2)
# print(r)
# print(list(r))
# if 10 not in r:
#     print('zai')
# else:
#     print("buzai")
# i = 0
# num = 0
# while i < 101:
#     if i % 2 == 0:
#         num += i
#     i += 1
# print(num)
# for i in range(100, 1000):
#     ge = i % 10
#     shi = i // 10 % 10
#     bai = i // 100
#     if i == (ge ** 3 + shi ** 3 + bai ** 3):
#         print(i)
# for i in range(3):
#     pwd = input("mima")
#     if pwd == '8888':
#         print("zhengque")
#         break
#     else:
#         print("budui ")
# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)
#
# for i in range(1, 51):
#     if i % 5 != 0:
#         continue
#     print(i)
# for i in range(3):  # 3行
#     for j in range(4):  # 4ge
#         print("*", end='\t')
#     print()
# for i in range(1, 10):
#     for j in range(i):
#         print(i, '*', j, '=', i * j, '; ', end='')
#     print()

# lst = ['a', 'b', 3, 1234]
# print(lst.index('a'))

# lst = [i*2 for i in range(1,6)]
# print(lst)
#
# scores = {}
# scores['a'] = 20
# scores['b'] = 120
# print(scores.values())
# print(list(scores.keys()))
# print(scores.items())
#
# print(scores.get("p"))
# print(scores.get("a"))
# print(scores['a'])
# print(scores['p'])
# item = ['apple', 'bear', 'banana', 'grape']
# price = [12, 45, 74, 66]
# dic = {item: price for item, price in zip(item, price)}
# print(dic)
s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {5, 8, 7, 9, 3, 10}
print(s1.intersection(s2))
print(s1 & s2)
print(s1.union(s2))
print(s1 | s2)
print(s1.difference(s2))
print(s1 - s2)
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

