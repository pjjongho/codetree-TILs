sum_1 = 0
avg_1 = 0
cnt = 0

for i in range(10):
    i = int(input())
    if i >=0 and i <= 200:
        sum_1 += i
        cnt += 1

avg_1 = sum_1/cnt

print(f'{sum_1} {avg_1:.1f}')