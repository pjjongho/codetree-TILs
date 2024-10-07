che =[0]*4

for i in range(3):
    a,b=input().split()
    b=int(b)
    if a =='Y'and b>=37:
        che[0]+=1
    elif a=='N' and b>=37:
        che[1]+=1
    elif a=='Y'and b<37:
        che[2]+=1
    elif a=='N'and b<37:
        che[3]+=1
for j in che:
    print(j,end=' ')

if che[0]>=2:
    print('E')