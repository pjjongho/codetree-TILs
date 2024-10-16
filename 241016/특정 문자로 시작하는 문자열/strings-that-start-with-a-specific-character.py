n = int(input())
lst = []
av = 0
cnt = 0

for i in range(n) :
    st = input()
    lst.append(st)
c = input()

for i in range(n) :
    if c == lst[i][0] :
        av += len(lst[i])
        cnt += 1

print(f"{cnt} {av/cnt:.2f}")