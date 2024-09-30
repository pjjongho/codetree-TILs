n = int(input())

for i in range(n):
    for j in range(n-(i+1)):
        print(" ", end="")
    for j in range((i * 2) +1):
        print("*", end="")
    print()

for i in range(0, n):   
    for _ in range(i+1):
        print(" ", end="")
    for _ in range((2 * n) - (2 * i)-n):
        print("*", end="")
    print()