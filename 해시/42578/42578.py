from itertools import combinations

def solution(clothes):
    answer = 0
    data = {}
    for i in clothes:
        if data.get(i[1]):
            data[i[1]] += 1
        else:
            data[i[1]] = 1
    if len(data.keys()) == 30:
        return 1073741823
    for i in range(0, len(data.keys())):
        for j in combinations(data.keys(), i + 1):
            temp = 1
            for k in j:
                temp *= data[k]
            answer += temp
    return answer


x = [["yellowhat", "headgear"]]
print(solution(x))