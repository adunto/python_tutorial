# 1) 질문: "Hello"와 "World"를 연결하여 "Hello World"를 출력하세요.
#              대문자로 변환하세요.
#             "Hello World"에서 "World"만 슬라이싱하여 출력하세요.
#              "Python is fun"에서 공백을 기준으로 문자열을 분리하세요.
#              "abcdef"에서 짝수 인덱스(0, 2, 4)의 문자들만 출력하세요.
#             "Hello"를 3번 반복하여 출력하세요.
# 파일명: string_process.py
# 실행: python string_proces.py
    # 결과: Hello World
        # HELLO WORLD
        # World
        # ['Python', 'is', 'fun']
        # ace
        # HelloHelloHello

w1 = "Hello"
w2 = "World"
str1 = w1 + ' ' + w2
str2 = "Python is fun"
str3 = "abcdef"

print(str1)
print(str.upper(str1))
print(str1.split(" ")[1])
print(str2.split(' '))
print(str3[::2])
print(w1 * 3)