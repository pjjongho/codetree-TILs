n, m = map(int, input(). split())

arr = [[0 for i in range(n)] for i in range(n)]

for i in range(1, m+1):
    a, b = map(int, input(). split())

    arr[a-1][b-1] = a*b

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i-1][j-1], end=' ')
    print()