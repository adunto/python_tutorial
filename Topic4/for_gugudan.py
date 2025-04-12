# 4) 구구단 3단을 출력하세요.
#      파일명: for_gugudan.py
#     실행: python for_gugudan.py
#     결과: 
#  3 × 1 = 3
#  3 × 2 = 6
#  3 × 3 = 9
#  3 × 4 = 12
#  3 × 5 = 15
#  3 × 6 = 18
#  3 × 7 = 21
#  3 × 8 = 24
#  3 × 9 = 27

def gugudan(num):
    
    for i in range(1, 10):
        print(f"{num} x {i} = {num*i}")
        
gugudan(3)