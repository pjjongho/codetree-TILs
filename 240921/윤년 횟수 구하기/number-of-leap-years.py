n = int(input())
cnt=0

for i in range(1,n):
    if i%4==0:
        cnt += 1
    elif i%100==0 and i%400!=0:
        cnt += 0
print(cnt)