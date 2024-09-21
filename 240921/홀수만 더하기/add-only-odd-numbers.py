sum_n = 0
for i in range(1,n+1):
    n = int(input())
    if n%2==1 and n%3==0:
        sum_n += i
print(sum_n)