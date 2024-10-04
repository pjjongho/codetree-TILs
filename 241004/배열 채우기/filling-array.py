n = list(map(int,input().split()))
lst = []

for i in range(len(n)):
    if n[i] ==0:
        break
    lst.append(n[i])
for i in lst[::-1]:
    print(i, end=' ')