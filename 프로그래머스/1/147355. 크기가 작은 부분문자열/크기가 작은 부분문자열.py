def solution(t, p):
    answer = 0
    
    num_p = int(p)
    
    for i in range(len(t) - len(p) + 1):
        num = t[i:len(p)+i] # 문자열만 slicing 가능
        
        if num_p >= int(num):
            answer += 1
            
    return answer