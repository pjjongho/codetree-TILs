n=list(map(int,input().split()))
lst =[]
sum_val = 0

for i in n:
    if i == 0:
        break
    sum_val += i
    lst.append(sum_val)
print(f'{sum_val} {sum_val/len(lst)}')