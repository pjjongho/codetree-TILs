arr = list(map(int,input().split()))
cnt = 0
sum_val = 0
sum_val2 = 0

for i in arr:
    if i%2==0:
        sum_val += i
    if i%3==0:
        sum_val2 +=i
        cnt += 1
print(f'{sum_val} {(sum_val2/cnt):.1f}')