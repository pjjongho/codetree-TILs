a, b = map(int,input().split())
start = 0
end = 0

for i in range(a,b+1):
    start = 0
    for j in range(1,i+1):
        if i%j==0:
            start += 1
    if start == 3:
        end += 1
print(end)