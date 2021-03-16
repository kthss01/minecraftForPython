# 절대경로 가져오기
import os.path
path = os.path.abspath("../chromedriver")
# print(path)

# 자동화 테스트를 위해 셀레니움(Selenium) 불러오기
from selenium import webdriver
from time import sleep

# 크롬 웹 드라이버 경로 설정
# driver = webdriver.Chrome(r'C:\Users\Kay\PycharmProjects\minecraftForPython\venv\chromedriver')
driver = webdriver.Chrome(path)

# 크롬을 통해 네이버 로그인 화면에 접속
driver.get('https://nid.naver.com/nidlogin.login')

# 여기부분은 일회용 로그인으로 수정
# # 아이디와 비밀번호 입력 (0.5초씩 기다리기, 너무 빠르면 트래픽 공격으로 취급될 수 있음)
# sleep(0.5)
# driver.find_element_by_name('id').send_keys('아이디')
# sleep(0.5)
# driver.find_element_by_name('pw').send_keys('비밀번호')
#
# # XPath를 이용해 로그인 시도
# driver.find_element_by_xpath('//*[@id="log.login"]').click()

sleep(0.5)
driver.find_element_by_xpath('//*[@id="log.otn"]').click()

sleep(0.5)
key = input('일회용 로그인 번호 입력: ')
driver.find_element_by_name('key').send_keys(key)

sleep(0.5)
driver.find_element_by_xpath('//*[@id="otnlog.login"]').click()

# 웹 페이지의 소스코드를 파싱하기 위해 Beautiful Soup 라이브러리 사용
from bs4 import BeautifulSoup

driver.get("https://mail.naver.com/")
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# 메일 제목을 하나씩 파싱
title_list = soup.find_all('strong', 'mail_title')

# 모든 메일 제목 출력
for title in title_list:
    print(title.text)