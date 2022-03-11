def solution(n, times):
    l, r = 0, 100000000000000
    while l < r:
        temp = 0
        mid = (l + r) // 2
        for i in times:
            temp += mid // i
        if temp < n:
            l = mid + 1
        else:
            r = mid
    return l