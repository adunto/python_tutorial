# 2) 질문: {"name": "John", "age": 30} 딕셔너리에서 "age"의 값을 출력하세요.
#              {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
#              딕셔너리 {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.
#      파일명: dict_process.py
#     실행: python dict_process.py
#     결과:  나이: 30
#              과목들: ['math', 'science', 'history'] 
#                 {'apple': 5, 'banana': 5}

dict1 = {
    "name": "John",
    "age": 30
}
print("나이: ", dict1["age"])

dict2 = {
    "math": 90,
    "science": 85,
    "history": 78
}

print("과목들: ", list(dict2.keys()))

dict3 = {
    "apple": 3,
    "banana": 5
}

dict3["apple"] = int(dict3["apple"]) + 2
print(dict3)