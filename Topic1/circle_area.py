#  1) 질문: 반지름 5인 원의 넓이를 계산하세요. (공식: 넓이 = π × 반지름², π=3.14) 
#  파일명: circle_area.py
#  실행: python bmi_calculator.py
#       결과: 체중(kg): 70
#       키(cm): 175
#       BMI: 22.9

import math

try:
    radius = input("반지름을 입력하세요: ")
    radius = float(radius)
    if radius < 0:
        raise ValueError("반지름은 음수가 될 수 없습니다.")
    
    area = math.pi * (radius ** 2)
    print("원의 넓이 : %.1f" % area)
except ValueError as e:
    print("잘못된 입력입니다:", e)

