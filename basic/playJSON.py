# Zhaoyu Wang developed
# time: 2023-04-03 3:57 p.m.
import json
data = [{'name':' 阿萨德', 'age':'21'}, {'name':'bb','age':'20'}, {'name':'cc','age':'22'}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)