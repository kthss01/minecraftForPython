# 자동 로그인 및 주요 정보 추출하기

import requests
from bs4 import BeautifulSoup as bs

MEMBER_DATA = {
    'memberID' : 'a',
    'memberPassword' : 'a'
}

# 하나의 세션(Sessino) 객체를 생성해 일시적으로 유지
with requests.Session() as s:
    # 로그인 페이지로의 POST 요청(Request) 객체 생성
    request = s.post('http://www.dowellcomputer.com/main.jsp', data=MEMBER_DATA)

# print(request.text)

request = s.get('http://dowellcomputer.com/member/memberUpdateForm.jsp?ID=a')
soup = bs(request.text, 'html.parser')

result = soup.findAll('input', {"name": "memberEmail"})
print(result[0].get('value'))