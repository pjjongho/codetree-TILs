n=int(input())
arr = list(map(int, input().split()))
cnt, result =0, 0
for idx, elim in enumerate(arr):
    if elim == 2:
        cnt+=1
        if cnt == 3:
            result = idx
print(result+1)