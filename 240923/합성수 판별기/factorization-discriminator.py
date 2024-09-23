n = int(input())

answer = False

for i in range(2, n):
    if n%i==0:
        answer=True
if answer==True:
    print('C')
else:
    print('N')