n = int(input())
arr = [1,n]

while True:
    for i in range(0,len(arr)):
        arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])

    if arr[len(arr) - 1] >= 100:
        break
print(*arr)