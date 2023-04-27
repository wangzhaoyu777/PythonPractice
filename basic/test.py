# import keyword
# a = keyword.kwlist
#
# print(len(a))
# print(a)
#
#
# print('aaaaa\taaaa')
# print('aaaaaa\taaaa')
# print('aaaaaaa\taaaa')
# print('aaaaaaaa\taaaa')
#
#
# print(chr(0b0111001110001011)+" 738b")
# print(chr(0b0110011011001100)+" 66cc")
# print(chr(0b0101101110000111)+" 5b87")

# name = 'Joey'
# age = 30
# print("My name is " + name , 'm' +str(age))
# a1 = '123'
# a2 = '12356.11'
# a3 = True
# a4 = 'asd'
# a5 = 645
# print(type(a1), type(a2), type(a3), type(a4), type(a5))
# print(float(a1), type(a1))
# print(float(a2), type(a2))
# print(float(a3), type(a3))
# # print(float(a4), type(a4))
# print(float(a5), type(a5))
"""
asd
asd
asd
"""
# list1 = []
#
# i = 0
# while i < 10:
#     list1.append(int(input('num')))
#     i += 1
# print(list1)
# [a, b, c] = [1, 2, 3]
# print(a)
# ----------------------------------------------------------------------
# Given 2 strings, needle and haystack, write a function that given the first index of string
# needle in haystack, and returns -1 if needle does not exist in haystack. use python
#
# needle = 'aa'
# haystack = 'asdgeaarg'
#
# def find_needle(needle: str, haystack: str) -> int:
#     """
#     Given a needle and haystack, return the first index of needle in haystack, or -1 if needle is not in haystack.
#     """
#     n_len = len(needle)
#     h_len = len(haystack)
#     if n_len > h_len:
#         return -1
#
#     for i in range(h_len - n_len + 1):
#         j = 0
#         while j < n_len and needle[j] == haystack[i + j]:
#             j += 1
#         if j == n_len:
#             return i
#
#     return -1
#
#
# # given a list , return max number in the list, python
# def find_max(numbers: list) -> int:
#     """
#     Given a list of numbers, return the maximum number.
#     """
#     return max(numbers)
#
# def find_max(numbers: list) -> int:
#     """
#     Given a list of numbers, return the maximum number.
#     """
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
#
# # given a string, return the count of each character in that string, python
# def count_chars(string: str) -> dict:
#     """
#     Given a string, return a dictionary where the keys are the characters in the string, and the values are the number of times each character appears.
#     """
#     char_counts = {}
#     for char in string:
#         if char in char_counts:
#             char_counts[char] += 1
#         else:
#             char_counts[char] = 1
#     return char_counts

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age
stu1 = Student('a', 12)
stu2 = Student('asd', 213)
print(stu1 > stu2)
print(stu1 < stu2)



