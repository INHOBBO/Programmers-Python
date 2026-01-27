def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number)-4):
        answer = answer + "*"
    for j in range(len(phone_number)-4, len(phone_number)):
        answer += phone_number[j]
        
    return answer

# 파이썬스럽게.
"""
def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]        
"""