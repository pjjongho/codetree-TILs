a, b = map(int,input().split())
cnt = 4
for i in range(2,9,2):
    for j in range(b,a-1,-1):
        print(f'{j} * {i} = {j*i}', end='')
        if j>a:
            print(' /', end=' ')
    print()
        
# a, b = map(int,input().split())

# for i in range(1,10):
#     for j in range(b, a-1,-2):
#         print(f'{j} * {i} = {j*i}', end='')
#         if j>a:
#             print(' /',end=' ')
#     print()