def solution(n):
    answer = []
    a = str(n)
    
    for i in a[::-1]:
        answer.append(int(i))
    
    return answer

"""
def solution(n):
    anwer = list(str(n))
    answer.reverse()
    
    return list(map(int, answer)) # map을 거치는 순간 map 객체가 되어서 다시 list로 형변환
"""