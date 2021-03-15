"""
pyautogui 연습
다른건 일단 넘어가고 메세지 박스만 이용
"""

import pyautogui as pg

a = pg.prompt(text='내용', title='제목', default='입력')
print(a)