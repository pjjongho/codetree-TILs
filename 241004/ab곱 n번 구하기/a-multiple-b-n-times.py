n = int(input())

for _ in range(n):
    inp = input()
    n = inp.split()
    a = int(n[0])
    b = int(n[1])
    ans = 1

    for i in range(a, b+1):
        ans *= i
    print(ans)