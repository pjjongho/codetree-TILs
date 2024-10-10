n=int(input())

MAP=[
    [0 for _ in range(n)]
    for _ in range(n)
]

number=1
for i in range(n):
    for j in range(n):
        MAP[j][i]=number
        number+=1
        

for row in MAP:
	for elem in row:
		print(elem, end=" ")
	print()