cn = input().split()
c = cn[0]
n = int(cn[1])
if c=='A':
    for i in range(1,n+1):
        print(i, end=" ")
else:
    if c=='D':
        for i in range(n,1,-1):
            print(i, end=" ")