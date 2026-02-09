def solution(number):
    answer = 0
    n = len(number)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer

""" 순열 이용
from itertools import combinations

def solution(number):
    answer = 0
    
    # number 배열에서 3개를 뽑는 모든 조합을 만듭니다.
    for trio in combinations(number, 3):
        # trio는 ( -2, 3, 0 ) 같은 튜플 형태입니다.
        if sum(trio) == 0:
            answer += 1
            
    return answer
"""