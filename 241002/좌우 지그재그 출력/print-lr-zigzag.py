Dislike
n = int(input())
# n * 2

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print((n * i) + (1 + j), end=" ")
        else:
            print((n * (i + 1)) - j, end=" ")
    print()