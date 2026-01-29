def solution(s):
    count_transform = 0 # 변환 횟수
    count_zeros = 0 # 제거된 0의 개수
    
    while s != '1':
        count_transform += 1
        
        # 1. 현재 문자열에서 '0'의 개수 찾아 누적
        num_zeros = s.count('0')
        count_zeros += num_zeros
        
        # 2. '0'이 제거된 후의 길이 구하기
        new_len = len(s) - num_zeros
        
        # 3. 길이를 2진법 문자열로 변환
        s = bin(new_len)[2:]
    
    return [count_transform, count_zeros]

