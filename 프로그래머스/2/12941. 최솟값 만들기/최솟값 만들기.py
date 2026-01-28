def solution(A,B):
    answer = 0

    # 배열 A는 오름차순, 배열 B는 내림차순으로 정렬해야 순서대로 곱할 때 최솟값!
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
            
    return answer