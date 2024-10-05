n = int(input())
grade = []
cnt = 0

for i in range(n):
    score = list(map(int,input().split()))
    grade.append(score)

for i in range(n):
    if sum(grade[i]) / 4 >=60:
        print('pass')
        cnt += 1
    else:
        print('fail')
        print(cnt)