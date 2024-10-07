n=int(input())
arr = list(map(int, input().split()))
cnt, result =0, 0
for idx, el in enumerate(arr):
    if el == 2:
        cnt+=1
        if cnt == 3:
            result = idx
print(result+1)