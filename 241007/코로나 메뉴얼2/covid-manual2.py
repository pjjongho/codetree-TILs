temp =[0]*4

for i in range(3):
    a,b=input().split()
    b=int(b)
    if a =='Y'and b>=37:
        temp[0]+=1
    elif a=='N' and b>=37:
        temp[1]+=1
    elif a=='Y'and b<37:
        temp[2]+=1
    elif a=='N'and b<37:
        temp[3]+=1
for j in temp:
    print(j,end=' ')

if temp[0]>=2:
    print('E')