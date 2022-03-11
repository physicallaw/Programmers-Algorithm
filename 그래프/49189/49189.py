from queue import Queue

def solution(n, edge):
    arr = [[]]
    check = [0] *(n+1)
    for i in range(n):
        arr.append([])
    for i, j in edge:
        arr[i].append(j)
        arr[j].append(i)
    check[1] = 1
    q = Queue()
    q.put(1)
    while len(q.queue):
        for i in arr[q.queue[0]]:
            if check[i] == 0:
                check[i] = check[q.queue[0]] + 1
                q.put(i)
        q.get()
    
    return check.count(max(check))