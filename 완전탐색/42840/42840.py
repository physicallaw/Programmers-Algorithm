def solution(answers):
    answer = []
    arr = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    for i in range(len(answers)):
        if s1[i] == answers[i]:
            arr[0] += 1
        if s2[i] == answers[i]:
            arr[1] += 1
        if s3[i] == answers[i]:
            arr[2] += 1
    for i in range(3):
        if arr[i] == max(arr):
            answer.append(i + 1)
    return answer
