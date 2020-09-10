# Hello Python
print("Hello Python")

# 주석은 #로
# 변수
a = 10
print(a)

# 사칙 연산
print(1 + 1)
print(a + 1)

# 문자열
print("1" + "1")
name = "Kim Tae Hun"
print(name)

print(a)
if a == 10 :
    print("a == 10")

# 조건문
name = "Kim Na Yeon"
# name = "not name"
print("name : " + name)

# 참고 리스트
name = ["Kim Tae Hun", "Kim Na Yeon"]

# if name == "Kim Tae Hun":
#     print("name is " + name)
# elif name == "Kim Na Yeon":
#     print("name is " + name)
# elif name == "Kim Tae Hun" or name == "Kim Na Yeon":
#     print("This is name")
if 'Kim Tae Hun' in name:
    print("This is name")
else:
    print("This is not name")

score = 80
if score >= 60:
    print("you are pass")
else:
    print("you are failed")

# 반복문 while
# while score >= 60:
#     print("score is " + str(score))
#     score -= 1

# while True:
#     if score == 60:
#         break
#     score -= 1
#     # 2로 나눈 나머지가 0 이란 의미는 짝수
#     if score % 2 == 0:
#         print(score)
#         continue

# 반복문 for
for i in name:
    print(i)

# 참고 튜플
a = [(1,2), (2,3), (4,5)]

for (x,y) in a:
    print(x,y)

scores = [30,40,50,60,70,80,90]
# for i in range(len(scores)):
#     print(scores[i])

i = 0
for score in scores:
    i = i+1
    if score >= 60:
        print("%d번 학생 합격 (%d)" % (i, score))
    else:
        print("%d번 학생 불합격 (%d)" % (i, score))

# range(10)은 0부터 10미만의 숫자를 포함
print(range(10))

# range(1,11) 시작숫자, 끝숫자 / 이 때 끝 숫자 포함 안됨
for i in range(1,11):
    print(i)

