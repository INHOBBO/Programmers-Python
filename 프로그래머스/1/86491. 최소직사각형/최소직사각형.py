def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        bigger = max(w, h)
        smaller = min(w, h)
        
        # 전체 명함 중 가장 긴 변 찾기
        if bigger > max_w:
            max_w = bigger
            
        # 전체 명함 중 가장 작은 변 찾기
        if smaller > max_h:
            max_h = smaller
            
        # 이렇게 하면 가장 긴 변, 가장 작은 변 찾게 됨 
            
    return max_w * max_h