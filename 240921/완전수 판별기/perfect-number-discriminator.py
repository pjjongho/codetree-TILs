n = int(input())
sum_ab = 0

for i in (1,n):
    if i%n==0:
        sum_ab += i
if sum_ab==n:
    print('P')
else:
    print('N')