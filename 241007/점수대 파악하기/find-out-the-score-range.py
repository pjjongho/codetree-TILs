arr = list(map(int,input().split()))
cnt_arr = [0]*11

for i in arr:
    if i == 0:
        break
    if i < 10:
        continue
    cnt_arr[i//10] += 1
    
for j in range(10,0,-1):
    print(f'{j}0 - {cnt_arr[j]}')