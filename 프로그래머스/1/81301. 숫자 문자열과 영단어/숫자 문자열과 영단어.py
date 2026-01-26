def solution(s):
    answer = 0
    
    words = {
        "zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
        "six":"6", "seven":"7", "eight":"8", "nine":"9"
    }
    
    # replace 학습!! 문자 > 문자로 바꿈
    for key, value in words.items():
        s = s.replace(key, value)
    
    return int(s)