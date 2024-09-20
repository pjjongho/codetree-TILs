n = int(input())

cnt = ''
while n<=100:
    if n>=90:
        cnt = 'A'
    elif n>=80:
        cnt = 'B'
    elif n>=70:
        cnt = 'C'
    elif n>=60:
        cnt = 'D'
    else:
        cnt = 'F'
    print(cnt, end=" ")
    n+=1