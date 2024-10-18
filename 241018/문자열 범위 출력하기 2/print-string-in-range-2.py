string = input()

a = int(input())

leng = len(string)
cnt = 0


for i in range(leng - 1, -1, -1):
	if cnt >= a:
		break
	print(string[i], end="")
	cnt += 1