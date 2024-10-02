n = int(input())

cnt = 2
for i in range(1,n+1):
    for j in range(n):
        print(cnt, end=' ')
        cnt += 2
        if cnt > 8:
            cnt=2
    print()