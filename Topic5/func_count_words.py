# 2)  문자열을 인자로 받아 단어 수를 반환하는 count_words 함수를 작성하세요.   
#      파일명: func_count_words.py


def count_words(s):
    print(f"단어 수 : {len(s.split(' '))}")

s = "python is very fun"

count_words(s)

