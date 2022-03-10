from itertools import permutations

def solution(numbers):
    arr = []
    for i in range(len(numbers)):
        for j in permutations(numbers, i + 1):
            arr.append(int(''.join(j)))
    dic = {}
    for i in arr:
        dic[i] = 1
    arr = list(dic.keys())
    prime = [True] * (max(arr) + 1)
    prime[0], prime[1] = False, False
    for i in range(2, len(prime)):
        for j in range(i * 2, len(prime), i):
            prime[j] = False
    answer = 0
    for i in arr:
        if prime[i]:
            answer += 1
    return answer