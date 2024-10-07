n, q = map(int, input().split())

elim = list(map(int, input().split()))

for _ in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        # a번째 원소 출력
        print(elim[lst[1]-1])
        
    elif lst[0] == 2:
        # 값이 b인 원소가 몇 번째 원소인지 찾기
        found = False
        for i in range(len(elim)):
            if elim[i] == lst[1]:
                print(i + 1)
                found = True
                break
        if not found:
            print(0)
            
    elif lst[0] == 3:
        # s번째 원소부터 e번째 원소까지 출력 (공백으로 구분)
        print(' '.join(map(str, elim[lst[1]-1:lst[2]])))