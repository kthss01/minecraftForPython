# 연속적인 크롤링 해보기

import requests
from bs4 import BeautifulSoup

# 한 건의 대화에 대한 정보를 담는 클래스
class Conversation:
    # 질문(Question), 응답(Answer) 두 변수로 구성
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"

# 모든 영어 대화 주제 추출하는 함수
def get_subjects():
    subjects = []

    # 전체 주제 목록을 보여주는 페이지로의 요청(Request) 객체 생성
    req = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.findAll('div', {"class": "tcb-col"})
    for div in divs:
        # 내부에 존재하는 <a> 태그들을 추출
        links = div.findAll('a')

        # <a> 태그 내부의 텍스트를 리스트에 삽입
        for link in links:
            subject = link.text
            subjects.append(subject)

    return subjects

subjects = get_subjects()
# print('총 ', len(subjects), '개의 주제를 찾았습니다.')
# print(subjects)

conversations = []
i = 1

# 모든 대화 주제 각각에 접근
for sub in subjects:
    print('(', i, '/', len(subjects), ')', sub)
    # 대화 스크립트를 보여주는 페이지로의 요청(Reuqest) 객체를 생성
    req = requests.get('https://basicenglishspeaking.com/' + sub)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    qnas = soup.findAll('div', {"class": "sc_player_container1"})

    # 각각의 대화 내용에 모두 접근
    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling
        else:
            a = qna.next_sibling
            c = Conversation(q, a)
            conversations.append(c)

    i = i + 1

print('총 ', len(conversations), '개의 대화를 찾았습니다.')

for c in conversations:
    print(str(c))
