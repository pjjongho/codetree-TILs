a = input().split()
a_g = a[0]
a_t = int(a[1])

b = input().split()
b_g = b[0]
b_t = int(b[1])

c = input().split()
c_g = c[0]
c_t = int(c[1])

if a_g=='Y' and a_t>=37:
    if b_g=='Y' and b_t>=37 or c_g=='Y' and c_t>=37:
        print("E")
    else:
        print('N')
elif b_g=='Y' and b_t>=37:
    if c_g=='Y' and c_t>=37:
        print('E')
    else:
        print('N')
else:
    print('N')