arr = [
    [0 for _ in range(10)]
    for _ in range(10)
]

n, m = tuple(map(int, input().split()))
	
for i in range(1, m + 1):
	r, c = map(int, input().split())
	arr[r][c] = i
			
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(arr[i][j], end=" ")
	print()