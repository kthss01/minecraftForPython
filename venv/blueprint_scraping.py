"""
마인크래프트 블루프린트(청사진) 스크래핑
타겟 사이트에서 마인크래프트 건축을 위한 블루프린트를 스크래핑을 하여
원하는 형태의 데이터로 가공하여 텍스트 파일로 저장하기
"""

import requests
import js2py
import pyautogui as pg
from bs4 import BeautifulSoup
from operator import itemgetter


# 메세지 박스로 url주소 입력 받기 위한 함수
# pyautogui 사용
def input_model_url():
    url = pg.prompt(
        text='마인크래프트 모델의 주소를 입력하세요 '
             'ex) https://www.grabcraft.com/minecraft/tiny-house/starter-houses',
        title='마인크래프트 블루프린트 스크래핑',
        default='https://www.grabcraft.com/minecraft/tiny-house/starter-houses')

    if url != None:
        return url + '#blueprints'
    else:
        return None


# 메세지 박스로 파일이름 입력 받기 위한 함수
# pyautogui 사용
def input_file_name(model_url):
    name = pg.prompt(
        text= '저장될 파일 이름을 입력하세요'
              '(확장자명 없이) ex) tiny-house',
        title='블루프린트 작성 완료',
        default=model_url)

    return name


# 블루프린트 스크래핑을 위한 함수
# 임포트시 호출
def blueprint_scraping():
    url = input_model_url()
    # url이 잘못되거나 cancel을 누를 시 프로그램 종료
    if url == None:
        return None
    # url = 'https://www.grabcraft.com/minecraft/tiny-house/starter-houses'

    response = requests.get(url)
    page = response.text
    # print(page)

    soup = BeautifulSoup(page, 'html.parser')

    # 원하는 태그 스크래핑
    js_url = soup.select('div.tab-content.blueprints script')[1]['src']
    # print(js_script)

    # js -> python 후 데이터 가공
    blueprint = blueprint_js_to_py(js_url)

    # default 파일 이름 url로부터 슬라이싱
    init_filename = url[url.find("minecraft/")+len("minecraft/"):-len("#blueprints")]

    # 파일로 저장
    # cancel을 누르지 않으면 실행 누르면 None 반환
    if input_file_name(init_filename) != None:
        write_blueprint(blueprint, filename)


# javascript 코드로된 blueprint를 python 코드로 전환 후
# 원하는 형태의 데이터로 가공하여 반환하는 함수
# 각 층별(layer별) 오름차순으로 정렬
def blueprint_js_to_py(js_url):
    js_code = requests.get(js_url).text

    # 자바스크립트 코드를 파이썬 코드로 전환
    layer_map = js2py.eval_js(js_code)
    # print(layer_map)

    # for layer in layer_map:
    #     print(layer)

    blueprint = {}

    # list내에 dictionary 정렬
    for key in layer_map:
        # print(key)
        layer = sorted(layer_map[key], key=itemgetter('x', 'y'))

        layer = change_offset(layer)

        # print(type(layer))
        # print(layer)

        blueprint[key] = layer

    # print(blueprint)
    # print(blueprint.keys())  # 각 layer 층 의미
    # print(blueprint['1'])

    return blueprint


# offsetX, offsetY 조정하는 함수
# left, top 기준 0,0으로 offset 조정
def change_offset(layer):
    offsetX = 5
    offsetY = layer[0]['y']  # 가장 처음의 작은 top을 기준

    for key in range(len(layer)):
        # print(layer[key])

        layer[key]['x'] = (layer[key]['x'] - offsetX) // 20
        layer[key]['y'] = (layer[key]['y'] - offsetY) // 20

    return layer


# 파일 쓰기 .txt로 저장
def write_blueprint(blueprints, filename):
    # for key in blueprints.keys():
    #     for blueprint in blueprints[key]:
    #         width = blueprint['x']
    #         height = blueprint['y']
    #         depth = int(key) - 1  # 계산 편하게 하기 위해 1층을 0으로
    #         block = blueprint['h']
    #         print("{}\t{}\t{}\t{}".format(width, height, depth, block))# for key in blueprints.keys():

    with open('{}.txt'.format(filename), 'w') as f:
        for key in blueprints.keys():
            for blueprint in blueprints[key]:
                width = blueprint['x']
                height = blueprint['y']
                depth = int(key) - 1  # 계산 편하게 하기 위해 1층을 0으로
                block = blueprint['h']
                f.write("{}\t{}\t{}\t{}\n".format(width, height, depth, block))


# 이 파이썬 파일로 실행시 실행 되는 부분
if __name__ == '__main__':
    # test
    # print(input_blueprint_name())

    blueprint_scraping()
