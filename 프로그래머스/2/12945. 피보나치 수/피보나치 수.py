def solution(n):
    # 0번째와 1번째 피보나치 수를 미리 설정
    fib = [0, 1]
    
    # 2번째부터 n번째까지 계산
    for i in range(2, n + 1):
        # (F[i-1] + F[i-2])를 계산한 뒤 즉시 1234567로 나눔
        # 값이 너무 커지는 것을 미연의 방지
        next_val = (fib[i-1] + fib[i-2]) % 1234567
        fib.append(next_val) # 리스트에 값을 입력할때는 append.
        
    return fib[n]