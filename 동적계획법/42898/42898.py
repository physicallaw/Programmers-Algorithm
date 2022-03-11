def solution(m, n, puddles):
    arr = []
    for i in range(m):
        arr.append([0] * n)
    arr[0][0] = 1
    for i, j in puddles:
        arr[i-1][j-1] = -1
    for i in range(1, m):
        if arr[i-1][0] == 1 and arr[i][0] != -1:
            arr[i][0] = 1
    for i in range(1, n):
        if arr[0][i-1] == 1 and arr[0][i] != -1:
            arr[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] != -1:
                arr[i][j] = max([arr[i-1][j]+arr[i][j-1], arr[i-1][j], arr[i][j-1]])

    return arr[m-1][n-1]%1000000007