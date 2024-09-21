a, b = map(int,input().split())

small = min(a,b)
large = max(a,b)

sum_ab=0

for i in range(small, large+1):
    if i%5==0:
        sum_ab += i

print(sum_ab)