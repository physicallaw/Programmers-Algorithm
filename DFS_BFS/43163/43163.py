from queue import Queue

def comp(a, b):
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
    return answer

def solution(begin, target, words):
    q = Queue()
    q.put([begin, 0])
    while len(q.queue) != 0:
        if q.queue[0][1] > len(words):
            return 0
        if q.queue[0][0] == target:
            return q.queue[0][1]
        for i in words:
            if comp(q.queue[0][0], i) == 1:
                q.put([i, q.queue[0][1]+1])
        q.get()
    return 0