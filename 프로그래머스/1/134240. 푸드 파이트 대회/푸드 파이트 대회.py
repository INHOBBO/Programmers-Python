def solution(food):
    answer = ""
    
    # 1. 1번 음식부터 마지막 음식까지 순회 (0번 물은 제외!)
    for i in range(1, len(food)):
        # 음식 번호(i)를 (개수 // 2)번 반복해서 더해줌
        answer = answer + str(i) * (food[i] // 2)
    
    # 2. 왼쪽 + 물(0) + 왼쪽을 뒤집은 것[::-1] 조립
    return answer + "0" + answer[::-1]






