def solution(n):
    num_3 = ""
    
    while n > 0:
        num_3 += str(n % 3)
        n //= 3
    
    return int(num_3, 3)