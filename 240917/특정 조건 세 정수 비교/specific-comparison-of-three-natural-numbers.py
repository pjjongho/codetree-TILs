arr = list(map(int,input().split()))

if arr[0]==min(arr) and arr[0]==arr[1]==arr[2]:
    print(1, 1)
else:
    print(0, 0)