arr=list(map(int,input().split()))
narr=[]

for i in arr:
    if i==999 or i==-999:
        break
    narr.append(i)
print(max(narr), min(narr))