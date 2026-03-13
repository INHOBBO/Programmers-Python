def solution(myString):
    words = myString.split('x')

    answer = [word for word in words if word]
    
    return sorted(answer)