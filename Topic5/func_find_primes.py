# 3)  시작값, 끝값을 인자로 받아 그 사이의 소수를 리스트로 반환하는 find_primes 함수를 작성하세요. 
#      파일명: func_find_primes.py

def find_primes(start, end):
    primes = []
    for n in range(start, end+1):
        if n > 1:
            isPrime = True
            
            for i in range(2, (n//2)+1):
                if n % i == 0:
                    isPrime = False
                    break
            
            if isPrime:
                primes.append(n)
                
    print(primes)
        
find_primes(2, 10)
        