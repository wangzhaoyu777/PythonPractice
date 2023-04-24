# Zhaoyu Wang developed
# time: 2023-04-23 2:28 p.m.
'''
练习地图可视化的基本应用
'''
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
#准备地图对象
map = Map()
#准备数据
data = [
    ('北京市',99),
    ('上海市',199),
    ('广东省',299),
    ('台湾省',399),
    ('湖北省',499),
]
#添加数据
map.add('test map', data, 'china')

#设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "10-500", "color": "#990033"},
        ]
    )
)
#绘图
map.render()