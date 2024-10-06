n = int(input())
arr = [1, n]

while True:
    # 새로 추가될 값을 미리 계산
    next_value = arr[-1] + arr[-2]
    
    # 100을 넘는 경우 그 값을 추가하고 종료
    if next_value > 100:
        arr.append(next_value)
        break
    
    arr.append(next_value)

# 결과 출력
print(*arr)