import math

def solution(n, m):    
    # 최대공약수
    # 1. 최대공약수(GCD) 구하기
    gcd = math.gcd(n,m)
    
    # 2. 최소공약수(LCM) 구하기
    lcm = n*m // gcd # 어차피 약수라 / 나 // 나 값은 똑같지만 / 실수형, //는 정수형!
    
    return [gcd,lcm]

""" 모듈 써서 쉽게 구하기
import math

def solution(n, m):
    # math.gcd()는 최대공약수, math.lcm()은 최소공배수
    # 단, math.lcm은 파이썬 3.9 버전부터 지원됩니다.
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd # 혹은 math.lcm(n, m)
    
    return [gcd, lcm]
"""