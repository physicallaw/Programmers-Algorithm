def solution(money):
    answer = 0
    arr1 = [money[0], max(money[0], money[1])]
    for i in range(2, len(money)):
        arr1.append(max(arr1[-3:-1]) + money[i])
    arr2 = [0, money[1]]
    for i in range(2, len(money)):
        arr2.append(max(arr2[-3:-1]) + money[i])
    return max(arr1[:-1]+arr2)