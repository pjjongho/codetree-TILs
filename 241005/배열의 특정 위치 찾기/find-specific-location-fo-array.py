arr = list(map(int,input().split()))
cnt = 0
filtered_arr1 = arr[1::2]
filtered_arr2 = arr[2::3]
sum_val = 0
sum_val2 = 0

for i in filtered_arr1:
    if i%2==0:
        sum_val += i

for i in filtered_arr2:
    if i%3==0:
        sum_val2 +=i
        cnt += 1

print(f'{sum_val} {(sum_val2/cnt):.1f}')