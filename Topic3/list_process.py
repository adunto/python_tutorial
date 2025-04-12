# 1) 질문: ["apple", "banana", "cherry"] 리스트에 "orange"를 추가하세요.
#              [10, 20, 30] 리스트의 모든 요소의 합을 구하세요.
#              [1, 2, 3, 4, 5] 리스트의 요소들을 역순으로 출력하세요.
#              [5, 2, 8, 1, 9] 리스트를 오름차순으로 정렬하세요.
#      파일명: list_process.py
#     실행: python list_process.py
#     결과:  ["apple", "banana", "cherry",”orange”] 
#               합계: 60
#                   [5, 4, 3, 2, 1]
#                   [1, 2, 5, 8, 9]

list = ["apple", "banana", "cherry"]

list.append("orange")
print(list)

sum = 0
for num in [10, 20, 30]:
    sum += num
print(f"합계: {sum}")

num_list1 = [1, 2, 3, 4, 5]
print(num_list1[::-1])

num_list2 = [5, 2, 8, 1, 9]
num_list2.sort()
print(num_list2)