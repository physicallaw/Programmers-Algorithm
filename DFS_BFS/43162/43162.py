from queue import Queue

def solution(n, computers):
    answer = 0
    check = [0] * n
    q = Queue()
    for i in range(n):
        if check[i]:
            continue
        answer += 1
        check[i] = 1
        q.put(i)
        while ~q.empty():
            for j in range(0, n):
                if ~computers[q.queue[0]][j] or check[j]:
                    continue
                check[j] = 1
                q.put(j)
            q.
            
    return answer