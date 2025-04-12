# 1)  두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요.    
#      파일명: func_calculator.py

#     calculator() 함수를 선언
#     	def calculator(a, b, op):


def calculator(n1, n2, op):
    if op == '+':
        return n1+n2
    elif op == '-':
        return n1-n2
    elif op == '*':
        return n1*n2
    elif op == '/':
        if n1 == 0 or n2 == 0:
            return 0
        return n1/n2
    else:
        print("올바르지 않은 형식")
        return

result = calculator(1, 2, '/')

print(result)