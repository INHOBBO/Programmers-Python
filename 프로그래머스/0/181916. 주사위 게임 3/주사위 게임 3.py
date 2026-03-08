def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)] 
        q = nums[counts.index(1)]
        return (10*p+q)**2
    elif max(counts) == 2:
        if min(counts) == 2:
            if a == b: # a, b가 같다 = c,d가 같다
                return (a+c)*abs(a-c)
            else: # a, c와 같고, b,d가 같다
                return (a+b)*abs(a-b)
        else: # 나머지 값은 다르다
            p = nums[counts.index(2)]
            return a*b*c*d / p**2 # 나머지 두 값의 곱임
    else:
        return min(nums)
        