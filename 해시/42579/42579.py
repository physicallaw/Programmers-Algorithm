def solution(genres, plays):
    answer, arr, cnt = [], {}, {}
    for i in range(len(genres)):
        if arr.get(genres[i]):
            arr[genres[i]].append([plays[i], i])
        else:
            arr[genres[i]] = [[plays[i], i]]
        if cnt.get(genres[i]):
            cnt[genres[i]] += plays[i]
        else:
            cnt[genres[i]] = plays[i]
    cnt = list(zip(cnt.keys(), cnt.values()))
    cnt.sort(reverse=True, key=lambda x: x[1])
    for i in cnt:
        arr[i[0]].sort(reverse = True, key=lambda x:(x[0], -x[1]))
        if len(arr[i[0]]) == 1:
            answer.append(arr[i[0]][0][1])
        else:
            answer.append(arr[i[0]][0][1])
            answer.append(arr[i[0]][1][1])
    return answer