def solution(n, lost, reserve):
    _reverse = sorted(list(set(reserve)-set(lost)))
    _lost = sorted(list(set(lost)-set(reserve)))
    
    for r in _reverse:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    
    return n-len(_lost)
        