"""
파이썬으로 자바스크립트 스크래핑 되는지 테스트
"""

import requests
import js2py

response = requests.get("https://h9y3q5u4.stackpathcdn.com/js/LayerMap/LayerMap_548.js")
# print(response.text)

js_code = response.text

layer_map = js2py.eval_js(js_code)
# print(layer_map)

# for layer in layer_map:
#     print(layer_map[layer])

# print(layer_map[1])

# list에서 dictionary 정렬
from operator import itemgetter

layer = sorted(layer_map[1], key=itemgetter('x', 'y'))

# print(layer)

blueprint = []

offsetX = 5
offsetY = layer[0]['y']

for data in layer:
    # print(data)
    block = data['h']
    x = (data['x'] - offsetX) // 20
    y = (data['y'] - offsetY) // 20
    print("{}\t{}\t{}\t{}".format(x,y,1,block))
