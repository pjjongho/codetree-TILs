n=int(input())
arr=[]
cnt=0
k=list(map(int, input().split()))
for i in range(n):
    if k[i]%2==0:
        cnt+=1
        arr.append(k[i])

for j in range(cnt-1,-1,-1):
    print(arr[j], end=' ')