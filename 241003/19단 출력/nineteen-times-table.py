n = 19

for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print(f'{i} * {j} = {i*j}',end='\n')
        elif j==19:
            print(f'{i} * {j} = {i*j}',end='')
        else:
            print(f'{i} * {j} = {i*j} /',end=' ')
    print()