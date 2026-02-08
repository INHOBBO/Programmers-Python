def solution(s):
    if len(s) == 4 or len(s) == 6:   
        for i in range(len(s)):
            # 각 글자가 숫자가 아니라면?
            if not s[i].isdigit(): # s[i].isdigit() == False
                return False
        return True # for문 안에 넣으면 정수가 처음에 앞쪽에 나오면 무조건 True가 되기에 다 돌리고 나서 True 출력!
    else:
        return False
        