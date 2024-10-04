n = list(map(int,input().split()))
i = 0
sum_val = 0

for i in range(len(n)):
    sum_val += n[i]
    if n[i] >= 250:
        sum_val -= n[i]
        i -= 1
        break

avg_val = sum_val/(i+1)
print(sum_val, f'{avg_val:.1f}')