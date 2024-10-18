a = input()
arr = []
arr_one = []
length = len(a)
cnt = 1

for i in range(1, length):
    if a[i]==a[i-1]:
        cnt+=1
        if i==length-1:
            arr.append(a[i])
            arr.append(cnt)       
    else:
        arr.append(a[i-1])
        arr.append(cnt)
        cnt=1
        if i==length-1:
            arr.append(a[i])
            arr.append(cnt)

str_a = ""
for i in arr:
    str_a += str(i)

if length==1:
    arr_one.append(a)
    arr_one.append(1)
    print(len(arr_one))
    for elem in arr_one:
        print(elem, end="")
else:
    print(len(str_a))
    print(str_a)