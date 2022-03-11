def solution(n, costs):
    answer = 0
    arr = [i + 1 for i in range(n)]
    costs.sort(key=lambda x:x[2])
    answer += costs[0][2]
    arr[costs[0][1]] = arr[costs[0][0]]
    for i in range(1, len(costs)):
        if arr[costs[i][0]] != arr[costs[i][1]]:
            answer += costs[i][2]
            t = arr[costs[i][1]]
            for j in range(len(arr)):
                if arr[j] == t:
                    arr[j] = arr[costs[i][0]]
        if min(arr) == max(arr):
            return answer