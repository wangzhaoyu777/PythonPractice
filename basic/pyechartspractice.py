# Zhaoyu Wang developed
# time: 2023-04-04 9:45 a.m.
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
#创建折线图对象
line = Line()
#给折线图对象添加x轴坐标
line.add_xaxis(['China', 'Canada', 'American'])

#给折线图Y轴坐标
line.add_yaxis('GDP',[30, 20, 10])

#设置全局标量
line.set_global_opts(
    title_opts=TitleOpts(title='GDdfgP', pos_left='center', pos_bottom='1%'),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

#通过render生成图像
line.render()