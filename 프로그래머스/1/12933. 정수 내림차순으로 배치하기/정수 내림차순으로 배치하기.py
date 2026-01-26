def solution(n):
    answer = list(map(int, str(n)))
    answer.sort(reverse=True)
    a = ""
    for i in answer:
        a += str(i)
    
    return int(a)