n = int(input())

for _ in range(1,n+1):
    a, b = map(int, input().split())  
    cnt = 0  
    for j in range(a, b + 1):
        if j % 2 == 0: 
            cnt += j
    print(cnt)