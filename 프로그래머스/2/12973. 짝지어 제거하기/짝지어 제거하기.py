def solution(s):
    answer = []
    
    for char in s:                           
        if answer and char == answer[-1]: # -1 인덱스는 맨 뒤, 이게 킥
            answer.pop()
        else:
            answer.append(char)
        
    return 1 if len(answer) == 0 else 0 
            