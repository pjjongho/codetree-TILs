n = int(input())

cnt = 9
for i in range(n+1,1,-1):
    for j in range(n):
        print(cnt, end='')
        cnt -= 1
        if cnt < 1:
            cnt=9
    print()