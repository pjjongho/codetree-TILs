a,b,c = map(int,input().split())
if a>=b:
    if b>=c:
        print(b)
    else:
        if a>=c:
            print(c)
        if a<c:
            print(a)
        if a<b:
            print(b)