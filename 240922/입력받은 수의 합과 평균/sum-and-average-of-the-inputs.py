sum_i=0
in2 = 0

n = int(input())

for i in range(n):
    in2 = int(input())
    sum_i += in2
    
print(f'{sum_i} {((sum_i)/n):.1f}')