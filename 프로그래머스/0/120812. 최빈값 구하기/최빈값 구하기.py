from collections import Counter

def solution(array):
    # Counter 객체를 생성하여 빈도수를 계산합니다
    counter = Counter(array)
    
    # 가장 높은 빈도의 값을 찾습니다.
    max_freq = max(counter.values())
    
    mode_candidates = []
    for k, v in counter.items():
        if v == max_freq:
            mode_candidates.append(k)
    
    if len(mode_candidates) > 1:
        return -1
    else:
        return mode_candidates[0]
    