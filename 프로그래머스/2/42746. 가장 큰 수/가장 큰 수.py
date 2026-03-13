def solution(numbers):
    number = list(map(str, numbers))
    number.sort(key = lambda x:x*3, reverse=True)
    
    answer = "".join(number) # 000이 나온다면?
    
    return str(int(answer))