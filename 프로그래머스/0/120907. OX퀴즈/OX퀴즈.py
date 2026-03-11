def solution(quiz):
    answer = []
    sol = []
    
    for i in range(len(quiz)):
        sol = quiz[i].split()
        if sol[1] == '+':
            result = int(sol[0]) + int(sol[2])
        else: # '-'
            result = int(sol[0]) - int(sol[2])
        
        if result == int(sol[4]):
            answer.append("O")
        else: # !=
            answer.append("X")
        sol = []
    return answer