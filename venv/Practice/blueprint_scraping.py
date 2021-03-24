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
        text='저장될 파일 이름을 입력하세요'
             '(확장자명 없이) ex) tiny-house',
        title='블루프린트 작성 시작',
        default=model_url)

    return name


# javascript 코드로된 blueprint를 python 코드로 전환 하는 함수
# js2py 사용
def blueprint_js_to_py(js_url):
    js_code = requests.get(js_url).text

    # 자바스크립트 코드를 파이썬 코드로 전환
    layer_map = js2py.eval_js(js_code)
    # print(layer_map)
    # print(type(layer_map))

    # for layer in layer_map:
    #     print(layer)

    return layer_map.to_dict()  # python dict 자료형으로 반환


# offsetY 구하는 함수
def find_offsetY(layer_map):
    ####### 가장 작은 offsetY 구하는데 오랜 시간이 걸림 해결방안 필요
    offsetY = layer_map['1'][0]['y']  # 가장 처음 top을 기준으로 잡고 시작

    for key in layer_map:
        for layer in layer_map[key]:
            # print(layer)
            offsetY = min(offsetY, layer['y'])

    return offsetY


# 문자열로 된 block 정보를 id와 data 값으로 바꿔주는 함수
def find_block(block_str):
    block_id = 0
    block_data = 0

    return block_id, block_data


# blueprint로 가공하여 파일로 저장
def make_blueprint(init_filename, layer_map):
    path = "./scraping/blueprints/"
    # 테스트를 위해 현재 위치에
    path = "./"

    filename = input_file_name(init_filename)
    # cancel을 누르면 None 반환
    if filename == None:
        # 파일 저장 취소
        return

    # 파일 저장
    f = open(path + '{}.txt'.format(filename), 'w')

    # 데이터 위치 가공
    # offset 구하기
    offsetX = 5
    offsetY = find_offsetY(layer_map)
    # print(offsetY)

    # print(layer_map)
    # print(type(layer_map))

    # dict의 key 값 정렬하여 list로 반환
    keylist = sorted(map(int, layer_map.keys()))
    keylist = map(str, keylist)  # 다시 문자열로 변환
    # print(keylist)
    for key in keylist:
        # 각 층별 list내의 block 정보 (dict) - x, y에 대하여 dict 정렬
        layer = sorted(layer_map[key], key=itemgetter('x', 'y'))

        # 각 block 가공
        for block in layer:
            # print(block)
            # block 위치 가공
            # offset의 맞게 x, y 값 변경
            width = (block['x'] - offsetX) // 20  # 경도 (longitude), 동(+), 서(-)
            depth = int(key) - 1  # 계산 편하게 하기 위해 1층을 0으로     # 표고 (elevation) 높낮이(0~255, 64 해수면)
            height = (block['y'] - offsetY) // 20  # 위도 (latitude), 남(+), 북(-)

            # block 정보 id와 data로 가공
            # block_str = block['h']
            # block_id = 0
            # block_data = 0
            block_id, block_data = find_block(block['h'])

            f.write("{}\t{}\t{}\t{}\t{}\n".format(width, depth, height, block_id, block_data))

    f.close()


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

    # js -> python 코드로 변경
    layer_map = blueprint_js_to_py(js_url)

    # 파일 저장 준비
    # default 파일 이름 url로부터 슬라이싱
    init_filename = url[url.find("minecraft/") + len("minecraft/"):-len("#blueprints")]

    # 데이터 가공하여 저장
    make_blueprint(init_filename, layer_map)


# 이 파이썬 파일로 실행시 실행 되는 부분
if __name__ == '__main__':
    # test
    # print(input_blueprint_name())

    blueprint_scraping()
