def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    dic = {}
    for i in citations:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    for i in range(10000,-1,-1):
        if dic.get(i):
            answer += dic[i]
        if answer >= i:
            return i