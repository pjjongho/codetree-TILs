def sum_num(n):
    num = 0
    for i in range(1,n+1):
        num += i
    print(f'{(num/10):.0f}')

n = int(input())
sum_num(n)