n, m = map(int,input().split())

def max_num(n,m):
    result = []
    for i in range(1,101):
        if i%n == 0 and i%m ==0:
            result.append(i)
    print(min(result))
max_num(n,m)