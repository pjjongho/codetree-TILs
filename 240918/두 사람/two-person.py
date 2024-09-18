a = input().split()
b = input().split()

a_age = int(a[0])
b_age = int(b[0])

if (a_age >= 19 and a[1] == 'M') or (b_age >= 19 and b[1] == 'M'):
    print(1)
else:
    print(0)