n, m = map(int,input().split())

def max_num(n,m):
    list = []
    for i in range(1,101):
        if i%n==0 and i%m==0:
            list.append(i)
    print(min(list))
        
max_num(n,m)