def solution(arr1, arr2):
    answer = []
    
    # 행
    for i in range(len(arr1)):
        row = [] # 임시 바구니
        # 열
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])

        answer.append(row)     
        
    return answer