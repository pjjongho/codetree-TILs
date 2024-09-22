a,b = map(int,input().split())
sum_ab = 0
for i in range(a,b+1):
    if i%6==0 and i%8 != 0:
        sum_ab += i
print(sum_ab)