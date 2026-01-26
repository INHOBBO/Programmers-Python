def solution(a, b, n):
    answer = 0
    
    while n >= a:
        # 1. 새로 받을 수 있는 콜라 계산
        new_cola = (n // a) * b
        
        # 2. 받은 콜라만큼 정답에 누적
        answer += new_cola
        
        # 3. 남은 빈 병 업데이트 (바꾸고 남은 거 + 새로 다 마신 거)
        n = (n % a) + new_cola
        
    return answer