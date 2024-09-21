cnt= 10
num = []

for _ in range(cnt):
    n = int(input())
    if n % 2 == 1:
        num.append(n)

print(len(num))