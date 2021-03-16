# 웹사이트에서 공지사항 웹 크롤링 해보기

import requests
from bs4 import BeautifulSoup

# 특정 URL에 접속하는 요청(Request) 객체를 생성
request = requests.get("http://www.dowellcomputer.com/main.jsp")

# 접속한 이후의 웹 사이트 소스코드 추출
html = request.text

# print(html)

# HTML 소스코드를 파이썬 객체로 변환
soup = BeautifulSoup(html, 'html.parser')

# <a> 태그 포함 요소 추출
links = soup.select('td > a')

# 모든 링크에 하나씩 접근
for link in links:
    # 링크가 href 속성을 가지고 있다면
    if link.has_attr('href'):
        # href 속성의 값으로 notice라는 문자열이 포함되어 있다면
        if link.get('href').find('notice') != -1:
            print(link.text)