def solution(bridge_length, weight, truck_weights):
    cnt, l = 0, 0
    arr = [0] * bridge_length
    for i in truck_weights:
        while cnt -arr[l] + i > weight:
            arr.append(0)
            cnt -= arr[l]
            l += 1
        arr.append(i)
        cnt += i - arr[l]
        l += 1

    return len(arr)