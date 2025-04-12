# 6)   두 리스트 [1, 2, 3]과 [4, 5, 6]의 각 요소를 더한 새 리스트를 생성하세요. (map 함수 사용)
#      파일명: map_func.py
#     실행: python map_func.py
#     결과: 
#      	[5, 7, 9]

list1 = [1, 2, 3]
list2 = [4, 5, 6]

r_list = list(map(lambda a, b: a + b, list1, list2))

print(r_list)