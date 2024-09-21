n = int(input())
sum_ab = 0

for i in range(1, n):
    if n % i == 0:
        sum_ab += i

if n == sum_ab:
    print("P")
else:
    print("N")