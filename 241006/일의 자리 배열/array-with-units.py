arr = []
inp = input().split()
arr.append(int(inp[0]))
arr.append(int(inp[1]))

for i in range(2,10) :
    arr.append((arr[i-1] + arr[i-2]) % 10)

for elem in arr :
    print(elem, end=" ")