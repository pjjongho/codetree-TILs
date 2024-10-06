# arr = list(map(int,input().split()))


# idx = 0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         idx = i

# for i in range(idx):
#     if arr[i]%2==0:
#         print(arr[i]//2, end=' ')
#     else:
#         print(arr[i]+3, end=' ')
    
arr = list(map(int, input().split()))

# 0을 제외하고 처리할 수 있도록 전체 리스트를 두 부분으로 나눈다
idx = arr.index(0)  # 0이 나오는 위치를 찾는다

# 0 이전의 숫자들 처리
for i in arr[:idx]:
    if i % 2 == 0:
        print(i // 2, end=' ')
    else:
        print(i + 3, end=' ')

# 0 이후의 숫자들 처리
for i in arr[idx+1:]:
    if i % 2 == 0:
        print(i // 2, end=' ')
    else:
        print(i + 3, end=' ')