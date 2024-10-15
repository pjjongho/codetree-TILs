n = int(input())

string = [
	input()
	for _ in range(n)
]

len_all = 0
cnt = 0
	
for i in range(n):
	len_all += len(string[i])
	if string[i][0] == 'a':
		cnt += 1
	
print(len_all, cnt)