a, b, c = map(int,input().split())
arr = [a,b,c]
sum_1 = sum(arr)
avg = (sum(arr))/len(arr)
print(sum_1)
print(int(avg))
print(int(sum_1-avg))