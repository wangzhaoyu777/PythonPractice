# Zhaoyu Wang developed
# time: 2023-05-07 6:35 p.m.
'''
练习python 递归操作
需求：通过递归，找出一个指定文件夹那的全部文件

思路：写一个函数，流出文件夹内的全部内容，如果是文件就收集到list
如果是文件夹，就递归调用自己，再次判断。
'''
import os

def test_os():
    '''掩饰os模块的3个基础方法'''
    print(os.listdir('D:/test'))        # 列出路径下的内容['a', 'b', 'test1.txt', 'test2.txt', 'test3.txt']
    print(os.path.isdir('D:/test/a'))   # 判断指定路径是不是文件夹True
    print(os.path.exists('D:/test'))    # 判断指定路径是否存在True

def get_files_recursion_from_dir(path):
    '''
    从指定的文件夹中是用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list，包含全部的文件，如果目录不存在或者无文件就返回一个空list
    '''
    # 进入到这里，表明这个目录是文件夹不是文件
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + '/' + f
            if os.path.isdir(new_path):
                # 进入到这里，表明这个目录是文件夹不是文件
                file_list+=get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f'当前{path}路径不正确')
        return []
    return file_list


if __name__ == '__main__':
    print(get_files_recursion_from_dir('D:/test'))



