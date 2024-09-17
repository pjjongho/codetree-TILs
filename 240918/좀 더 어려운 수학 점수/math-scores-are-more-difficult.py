inp = input()
arr = inp.split()
m_a = int(arr[0])
e_a = int(arr[1])

inp = input()
arr = inp.split()
m_b = int(arr[0])
e_b = int(arr[1])

if m_a==m_b:
    if e_a>e_b:
        print('A')
    else:
        print('B')
else:
    if m_a>m_b:
        print('A')
    else:
        print('B')