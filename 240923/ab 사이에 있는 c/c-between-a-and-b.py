a, b, c = map(int,input().split())

answer = False
for i in range(a,b+1):
    if i%c==0:
        answer = True

if answer==True:
    print('YES')
else:
    print('NO')