# Zhaoyu Wang developed
# time: 2023-04-25 2:34 p.m.
from pyecharts.charts import Bar

# 构建柱状图
bar = Bar()
# 添加X轴数据
bar.add_xaxis(['中国','美国','英国'])
# 添加Y轴数据
bar.add_yaxis('GDP', ['30', '20', '10'])
# render
bar.render('基础柱状图.html')