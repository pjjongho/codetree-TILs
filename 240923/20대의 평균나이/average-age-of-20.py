cnt = 0
sum_age = 0

while True:
    n = int(input())
    if n<20 or n>=30:
        print(f'{sum_age/cnt:.2f}')
        break
    sum_age += n
    cnt += 1