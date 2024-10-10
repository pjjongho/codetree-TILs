n, m = map(int, input().split())
array1 = [list(map(int, input().split())) for _  in range(n)]
array2 = [list(map(int, input().split())) for _  in range(n)]

for i in range(n):
    for j in range(m):
        if array1[i][j] == array2[i][j]:
            array1[i][j] = 0
        else:
            array1[i][j] = 1

for i in range(n):
    for j in range(m):
        print(array1[i][j], end=' ')
    print()