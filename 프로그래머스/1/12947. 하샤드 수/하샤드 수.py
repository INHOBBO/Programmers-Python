def solution(x):
    answer = 0
    # 숫자 % 각 자리수 합  = 0 햐샤드 수
    a = str(x)
    
    for i in a:
        answer = answer + int(i) 
    
    if x % answer == 0:
        return True
    else:
        return False