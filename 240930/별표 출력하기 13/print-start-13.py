n = int(input())
a,b = n,1

for i in range(2*n):
    if i%2==0:
        print('* '*a, end=" ")
        a -=1
    else:
        print('* '*b,end=" ")
        b +=1
    print()