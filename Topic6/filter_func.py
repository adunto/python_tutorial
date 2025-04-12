# 2)  [10, 20, 30, 40, 50]에서 30보다 큰 수만 필터링하세요. 
#         (filter 함수 사용)   
#      파일명: filter_func.py
#     실행: python filter_func.py
#     결과: [40, 50]

num_list = [10, 20, 30, 40, 50]

filtered_list = list(filter(lambda n: n > 30, num_list))

print(filtered_list)