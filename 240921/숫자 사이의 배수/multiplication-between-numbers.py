a, b = map(int,input().split())

sum_ab = 0
avg_ab = 0
cnt=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sum_ab += i
        cnt += 1
print(f'{sum_ab} {(sum_ab/cnt):.1f}')