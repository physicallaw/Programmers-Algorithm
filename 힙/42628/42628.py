from queue import PriorityQueue

def solution(operations):
    answer = [0, 0]
    n = 0
    q1, q2 = PriorityQueue(), PriorityQueue()
    for i in operations:
        arr = i.split()
        if arr[0] == 'I':
            q1.put(-int(arr[1]))
            q2.put(int(arr[1]))
            n += 1
        else:
            if n == 0:
                continue
            if i.split()[1] == '1':
                q1.get()
            else:
                q2.get()
            n -= 1
            if n == 0:
                q1.queue.clear()
                q2.queue.clear()
    if n != 0:
        answer = [-q1.get(), q2.get()]
    return answer