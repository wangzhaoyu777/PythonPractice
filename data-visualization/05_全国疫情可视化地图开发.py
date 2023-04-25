# Zhaoyu Wang developed
# time: 2023-04-24 6:06 p.m.
'''
练习全国疫情可视化地图开发
'''
from pyecharts.charts import Map
from pyecharts.options import *
import json
# 读取数据文件
f = open('D:/疫情.txt','r', encoding='UTF-8')
data = f.read()
# 关闭文件
f.close()
# 取到各省份数据
# 将JSON转化为python字典
data_dict = json.loads(data) #基础数据字典
# 从字典中取省份数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元祖，并封装各个省份的数据在列表内
data_list = []
for province_data in province_data_list:
    if province_data["name"]=='北京' or province_data["name"]=='上海' or province_data["name"]=='重庆':
        province_name = province_data["name"] + '市'
    elif province_data["name"]=='澳门' or province_data["name"]=='香港':
        province_name = province_data["name"] + '特别行政区'
    elif province_data["name"]=='内蒙古' or province_data["name"]=='西藏':
        province_name = province_data["name"] + '自治区'
    elif province_data["name"]=='新疆':
        province_name = province_data["name"] + '维吾尔自治区'
    elif province_data["name"]=='广西':
        province_name = province_data["name"] + '壮族自治区'
    elif province_data["name"]=='宁夏':
        province_name = province_data["name"] + '回族自治区'
    else:
        province_name = province_data["name"] + '省'
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)
# 创建地图对象
map = Map()
# 添加数据
map.add("省份确诊人数", data_list, "china")
# 设置全局配置，定制分段视觉影射
map.set_global_opts(
    title_opts=TitleOpts(title='疫情全国地图'),
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
map.render("全国疫情地图.html")

