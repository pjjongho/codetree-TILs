n = int(input())

for i in range(n):
    if i==0:
        print('*',end=' ')
    else:
        for j in range(n-2):
            if i>0:
                print(' ', end=' ')
print()