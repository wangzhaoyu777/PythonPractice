# Zhaoyu Wang developed
# time: 2023-05-01 11:19 a.m.
import json

from Data_analysis_proj.data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        '''读取文件数据，把读取到的每一条都转换为Record类型的对象，将他们封装到list并返回'''
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path        # 定义成员变量记录文件路径

    # 复写实现抽象父类中的方法
    def read_data(self) -> list[Record]:
        record_list :list[Record]=[]
        f = open(self.path, 'r', encoding='UTF-8')
        for line in f.readlines():
            line = line.strip()     # 消除读取到的每一行\n
            data_list = line.split(',')
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self) -> list[Record]:
        record_list :list[Record]=[]
        f = open(self.path, 'r', encoding='UTF-8')
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader('D:/自学/黑马python/2011年1月销售数据.txt')
    json_file_reader = JsonFileReader('D:/自学/黑马python/2011年2月销售数据JSON.txt')
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
