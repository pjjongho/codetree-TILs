n = int(input())
sum_ab = 0

for i in range(1,n+1):
    if i%n==0:
        sum_ab += i
if sum_ab==n:
    print('P')
else:
    print('N')