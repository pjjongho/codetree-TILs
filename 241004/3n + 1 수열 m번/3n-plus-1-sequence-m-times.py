m = int(input())


for _ in range(m):
    n = int(input())
    cnt = 0
    for _ in range(n, 10000):
        if n==1:
            print(cnt)
            break
        if n%2==0:
            n //= 2
        else:
            n = 3 * n + 1
        cnt += 1