n = int(input())

for i in range(n,0,-1):
    for j in range(i-1,n):
        j+=1
        print(j, end=' ')
    print()