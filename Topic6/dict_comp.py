# 5)   ["apple", "banana", "cherry"]에서 각 단어의 길이를 딕셔너리로 만드세요. (딕셔너리 컴프리헨션 사용)
#      파일명: dict_comp.py
#     실행: python dict_comp.py
#     결과: 
#      	{'apple': 5, 'banana': 6, 'cherry': 6}

t_list = ["apple", "banana", "cherry"]
r_dic = {word: len(word) for word in t_list}

print(r_dic)
