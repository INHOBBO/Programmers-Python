def solution(s):
    answer = []
    
    for char in s.split(' '):
        word = ''
        for i in range(len(char)):
            if i % 2 == 0: # 짝수 
                word += char[i].upper()
            else: # 홀수
                word += char[i].lower()
        answer.append(word)
                
    return ' '.join(answer)