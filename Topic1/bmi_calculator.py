# 2) 질문: 사용자로부터 체중(kg)과 키(cm)를 입력받아 BMI를 계산하세요. 
#         (공식: BMI = 체중(kg) / (키(m)²))
#    파일명: bmi_calculator.py

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("양수를 입력해야 합니다.")
            return value
        except ValueError as e:
            print("잘못된 입력입니다:", e)

weight = get_positive_float("체중을 입력하세요(kg): ")
height = get_positive_float("키를 입력하세요(cm): ")

height_m = height / 100
bmi = weight / (height_m ** 2)
print("bmi = " + str("%.1f" % bmi))