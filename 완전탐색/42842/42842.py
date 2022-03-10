def solution(brown, yellow):
    l = 3
    while True:
        r = (brown - (l - 2) * 2) // 2
        if (l - 2) * (r - 2) == yellow:
            return [r, l]
        l += 1