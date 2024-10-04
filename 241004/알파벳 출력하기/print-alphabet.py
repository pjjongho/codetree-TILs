k=65
n=int(input())
for i in range(n):
    for _ in range(i+1):
        if k != ord('Z'):
            print(chr(k), end='')
            k+=1
        if k >= ord('Z'):
            print(chr(k), end='')
            k=ord('A')
    print()