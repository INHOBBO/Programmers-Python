def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        sliced = array[i-1:j]
        sorted_list = sorted(sliced)
        answer.append(sorted_list[k-1])
    
    return answer