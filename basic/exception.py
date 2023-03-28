# Zhaoyu Wang developed
# time: 2023-03-21 10:25 a.m.
import traceback

try:
    print('--------------------')
    print(10/0)
except:
    traceback.print_exc()

