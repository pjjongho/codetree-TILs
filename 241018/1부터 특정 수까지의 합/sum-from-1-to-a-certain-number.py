import math

def sum_num(n):
    num = 0
    for i in range(1,n+1):
        num += i
    print(f'{math.floor(num/10)}')

n = int(input())
sum_num(n)