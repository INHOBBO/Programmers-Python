def solution(k, score):
    answer = []
    hall_of_fame = [] # 명예의 전당
    
    for s in score:
        hall_of_fame.append(s) # 일단 입장!
        hall_of_fame.sort(reverse=True) # 점수순으로 줄 세우기
        
        # 의자가 k개보다 많아지면 꼴찌(k번째 이후)는 탈락!
        if len(hall_of_fame) > k:
            hall_of_fame.pop() # 마지막 요소 제거
            
        # 현재 명예의 전당 멤버 중 꼴찌(-1번째) 점수를 기록
        answer.append(hall_of_fame[-1])
        
    return answer