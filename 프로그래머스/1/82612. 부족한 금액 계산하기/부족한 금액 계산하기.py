def solution(price, money, count):
    total_price = 0
    
    for i in range(1, count+1):
        total_price += price*i
    
    result = money - total_price
    
    if result < 0:
        return abs(result)
    else:
        return 0