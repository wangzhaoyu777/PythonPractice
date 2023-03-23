# Zhaoyu Wang developed
# time: 2023-03-20 5:25 p.m.
# n1 = 10
# n2 = [11, 22, 33]
# def fun(a, b):
#     print('a=', a)
#     print('b=', b)
#     a = '100'
#     b.append(10)
#     print('a=', a)
#     print('b=', b)
# fun(n1, n2)
# def fun(num):
#     odd = []
#     even = []
#     for i in num:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return odd, even
#
# lst = [11, 22, 33, 55, 321, 20, 30, 6541, 84]
# print(fun(lst))
# def fac(n):
#     if n ==1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(6))
def fab(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(6))


lst = []
for i in range(1, 9):
    a = fab(i)
    lst.append(a)
    print(lst)





