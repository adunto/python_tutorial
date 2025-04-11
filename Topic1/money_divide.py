# 4) 질문: 10000원을 3명이서 똑같이 나누어 가질 때 각자 얼마를 받고 얼마가 남는지 계산하세요.
# 파일명: money_divide.py

def divide_money(money, p_count=3):

    per_money = int(int(money) / 3)

    return (per_money, money - (per_money * p_count))
    
per_money, remain = divide_money(money=10000)

print(f'각자 받는 돈 : {per_money}')
print(f'남은 돈 : {remain}')