def solution(s):
    answer = []
    
    for i in range(len(s)):
        if s[i] not in s[0:i]:
            answer.append(-1)
        else:
            # 현재 인덱스 - 나온 단어 인덱스
            #"내 앞부분(s[:i])에서, 지금 내 글자(s[i])가 어디 있는지 뒤에서부터 거꾸로 찾아줘!"
            last_index = s[0:i].rfind(s[i])
            answer.append(i-last_index)
               
    return answer