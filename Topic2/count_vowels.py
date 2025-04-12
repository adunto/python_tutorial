# 4) 질문: "Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.
#      파일명: count_vowels.py
#     실행: python count_vowels.py
#     결과: 모음 개수 : 6

def aeiou_counter(s):
    list = ['a', 'e', 'i', 'o', 'u']
    count=0
    
    for item in list:
        
        count += str(s).count(item)
        
    print(f"모음 개수 : {count}")
    
aeiou_counter("Python is awesome")