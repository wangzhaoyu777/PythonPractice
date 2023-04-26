# Zhaoyu Wang developed
# time: 2023-04-25 3:49 p.m.
# Zhaoyu Wang developed
# time: 2023-04-25 2:34 p.m.
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 构建柱状图
bar1 = Bar()
bar1.add_xaxis(['中国','美国','英国'])
bar1.add_yaxis('GDP', ['30', '20', '10'], label_opts=LabelOpts(position='right'))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['中国','美国','英国'])
bar2.add_yaxis('GDP', ['60', '30', '20'], label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['中国','美国','英国'])
bar3.add_yaxis('GDP', ['90', '60', '30'], label_opts=LabelOpts(position='right'))
bar3.reversal_axis()
# 构建时间对象
timeline = Timeline({'theme': ThemeType.ROMA})
# 在时间线内添加柱状图对象
timeline.add(bar1, '点1')
timeline.add(bar2, '点2')
timeline.add(bar3, '点3')

# 自动播放设置
timeline.add_schema(
    play_interval=1000,     #自动播放时间间隔毫秒
    is_timeline_show=True,  #是否显示时间线
    is_auto_play=True,      #是否自动播放
    is_loop_play=True       #是否循环播放
)
# 主题设

# render
# 绘图要用时间线对象，而不是bar 对象
timeline.render('基础时间线图.html')