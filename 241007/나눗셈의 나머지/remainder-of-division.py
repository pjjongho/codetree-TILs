a, b = tuple(map(int, input().split()))

arr = []

while True:

    if a <= 1:
        break
    div = a % b
    a //= b
    arr.append(div)


count_arr = [0] * 10

for elem in arr:
    count_arr[elem] += 1


result = 0

for i in range(10):

    result += count_arr[i] ** 2

print(result)