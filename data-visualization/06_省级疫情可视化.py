# Zhaoyu Wang developed
# time: 2023-04-25 10:03 a.m.
'''
练习河南省疫情地图开发
'''
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open('D:/疫情.txt','r', encoding='UTF-8')
data = f.read()
# 关闭文件
f.close()
# 获取河南省数据
# json数据转为字典
data_dict = json.loads(data)
# 取到河南数据
cities_data = data_dict['areaTree'][0]['children'][17]['children']
# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data['name'] + '市'
    city_confirm = city_data['total']['confirm']
    data_list.append((city_name, city_confirm))
print(data_list)
# 构建地图
map = Map()
map.add('辽宁分布', data_list, "辽宁")
# 设置全局变量
map.set_global_opts(
    title_opts=TitleOpts(title='疫情辽宁地图'),
    visualmap_opts=VisualMapOpts(
        is_show=True,   # 是否分段
        is_piecewise=True,   # 是否显示
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)
# 绘图
map.render('辽宁省疫情地图.html')
