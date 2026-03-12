def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        if s[i].isupper():
            answer += chr((ord(s[i]) + n - ord('A')) % 26 + ord('A'))
        elif s[i].islower():
            answer += chr((ord(s[i]) + n - ord('a')) % 26 + ord('a'))

    return answer