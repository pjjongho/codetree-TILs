n = list(map(int,input().split()))
cnt = 0
sum_val = 0
for i in n:
    if i%2==0:
        cnt += 1
        sum_val += i
    if i==0:
        cnt -= 1
        break
    
print(cnt, sum_val)