a, b = map(int,input().split())

if a>0:
    for _ in range(b):
        print(a,end="")
else:
    if a<0:
        print(0)