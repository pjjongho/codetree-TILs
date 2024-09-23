n = int(input())
answer = True

for i in range(2,n):
    if n%i==0:
        answer=False
if answer==True:
    print('P')
else:
    print('C')